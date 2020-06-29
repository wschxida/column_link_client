#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : column_link.py
# @Author: Cedar
# @Date  : 2020/4/22
# @Desc  :

import time
import asyncio
import aiohttp
from lxml import etree
from requests.compat import urljoin
import lib.common as common
import warnings
import sqlite3
import os


# 忽略mysql插入时主键重复的警告
warnings.filterwarnings('ignore')
tasks = []
conn = sqlite3.connect('test.db')
c = conn.cursor()


async def get_response(semaphore, url, column_extraction_deep=1, domain_code_source=None, host_code_source=None, website_no=None):
    async with semaphore:
        timeout = aiohttp.ClientTimeout(total=10)
        connector = aiohttp.TCPConnector(limit=60, verify_ssl=False)  # 60小于64。也可以改成其他数
        async with aiohttp.ClientSession(timeout=timeout, connector=connector) as session:
            try:
                headers = {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
                }
                async with session.get(url, headers=headers) as response:
                    text = await response.text()
                    root = etree.HTML(text, parser=etree.HTMLParser(encoding='utf-8'))
                    print(url)
                    column_extraction_deep = int(column_extraction_deep) + 1

                    items = root.xpath('//a')
                    column_list = []
                    # print(len(items))
                    for item in items:
                        title = "".join(item.xpath('.//text()'))
                        listpage_url = "".join(item.xpath('./@href'))
                        listpage_url = urljoin(url, listpage_url)
                        record_md5_id = common.get_token(listpage_url)
                        # 去掉标点符号
                        title = common.filter_punctuation(title)
                        listpage_url = common.match_url(listpage_url)
                        domain_code = common.get_domain_code(listpage_url)
                        host_code = common.get_host_code(listpage_url)
                        # domain 要与源域名一致
                        if domain_code_source != domain_code:
                            continue
                        if host_code_source != host_code:
                            continue

                        # 垃圾词、垃圾域名过滤
                        status, level_score = common.is_need_filter(title, listpage_url, False)
                        print(status, level_score)

                        if level_score > 0:
                            column = f"('{title}', '{listpage_url}', '{record_md5_id}', '{website_no}', {column_extraction_deep}, '{domain_code}', '{host_code}', '{level_score}')"
                            column_list.append(column)

                    # 批量插入
                    values = ",".join(column_list)
                    insert_column = f"insert or ignore into column_link_client(Title, URL, record_md5_id, website_no, column_extraction_deep, domain_code, host_code, level_score) values{values};"
                    # print(insert_column)
                    try:
                        c.execute(insert_column)
                        conn.commit()
                    except Exception as e:
                        pass

            except Exception as e:
                print(e)


async def create_task():
    semaphore = asyncio.Semaphore(100)  # 限制并发量为 100

    # 查询待采集目标
    website_no = ('S_50', '')
    select_column_count = f"select count(1)" \
                          f"from column_link_client where website_no in{website_no} and Extracted_flag is null " \
                          f"ORDER BY Column_Extraction_Deep limit 100;"
    try:
        column_count = c.execute(select_column_count)
        for i in column_count:
            print(i[0])
            if i[0] < 1:
                os._exit(0)
    except Exception as e:
        pass

    select_column = f"select Column_Link_ID, Column_Extraction_Deep, URL, Domain_Code, host_code, Website_No, Extracted_flag " \
                    f"from column_link_client where website_no in{website_no} and Extracted_flag is null " \
                    f"ORDER BY Column_Extraction_Deep limit 100;"
    print(select_column)
    try:
        results = c.execute(select_column)
        # 更新Extracted_flag
        id_list = [0]
        for result in results:
            print(result)
            id_list.append(result[0])
            column_extraction_deep = result[1]
            url = result[2]
            domain_code = result[3]
            host_code = result[4]
            website_no = result[5]
            if not column_extraction_deep:
                column_extraction_deep = 0
            # 最多采集3层
            if column_extraction_deep < 3:
                task = asyncio.ensure_future(
                    get_response(semaphore, url, column_extraction_deep, domain_code, host_code, website_no))
                tasks.append(task)
        id_list = tuple(id_list)
        update_flag = f"update column_link_client set Extracted_flag='S' where Column_Link_ID in {id_list};"
        try:
            c.execute(update_flag)
            conn.commit()
        except Exception as e:
            print(e)

    except Exception as e:
        pass


def run():
    for j in range(1, 20000):
        print(j)
        print(time.time())
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        global tasks
        tasks = []
        loop.run_until_complete(create_task())
        loop.run_until_complete(asyncio.gather(*tasks))
        loop.close()
        time.sleep(2)


if __name__ == '__main__':
    run()
    conn.close()
