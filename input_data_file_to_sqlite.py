#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : input_data_file_to_sqlite.py
# @Author: Cedar
# @Date  : 2020/4/21
# @Desc  :


import lib.common as common
import sqlite3


def main():
    fn = open('website.txt', 'r', encoding='UTF-8')  # 打开文件
    column_list = []
    for i in fn:
        title = i.split('=')[0].strip()
        listpage_url = i.split('=')[1].strip()
        record_md5_id = common.get_token(listpage_url)
        website_no = 'S_50'
        column_extraction_deep = 0
        domain_code = common.get_domain_code(listpage_url)
        host_code = common.get_host_code(listpage_url)
        level_score = 100
        column = f"('{title}', '{listpage_url}', '{record_md5_id}', '{website_no}', {column_extraction_deep}, '{domain_code}', '{host_code}', '{level_score}')"
        column_list.append(column)
        print(column)

    fn.close()  # 关闭文件

    # 批量插入
    values = ",".join(column_list)
    insert_column = f"insert or ignore into column_link_client(Title, URL, record_md5_id, website_no, column_extraction_deep, domain_code, host_code, level_score) values{values};"
    print(insert_column)
    try:
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute('delete from column_link_client;')
        conn.commit()
        c.execute(insert_column)
        conn.commit()
        conn.close()
    except Exception as e:
        pass


if __name__ == '__main__':
    main()
