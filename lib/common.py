#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : common.py
# @Author: Cedar
# @Date  : 2020/4/23
# @Desc  :


import time
import json
from datetime import datetime
import hashlib
from requests.compat import urljoin
import pymysql
import re
import tldextract
import reject_domain
import reject_junkword
import custom_str_invalid
import custom_keyword_score


def get_token(md5str):
    # md5str = "abc"
    # 生成一个md5对象
    m1 = hashlib.md5()
    # 使用md5对象里的update方法md5转换
    m1.update(md5str.encode("utf-16LE"))
    token = m1.hexdigest()
    return token


def query_mysql(config_params, query_sql):
    """
    执行SQL
    :param config_params:
    :param query_sql:
    :return:
    """
    # 连接mysql
    config = {
        'host': config_params["host"],
        'port': config_params["port"],
        'user': config_params["user"],
        'passwd': config_params["passwd"],
        'db': config_params["db"],
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor
    }
    results = None
    try:
        conn = pymysql.connect(**config)
        conn.autocommit(1)
        # 使用cursor()方法获取操作游标
        cur = conn.cursor()
        cur.execute(query_sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        conn.close()  # 关闭连接
    except Exception as e:
        pass

    return results


def get_domain_code(url):
    domain_code = ''
    domain_info = tldextract.extract(url)
    # print(domain_info)
    if domain_info.domain:
        if is_ip(domain_info.domain):
            domain_code = domain_info.domain
        elif domain_info.suffix:
            domain_code = f"{domain_info.domain}.{domain_info.suffix}"
            if domain_code.find('%') > -1:
                domain_code = ''
    return domain_code.strip('.')


def get_host_code(url):
    host_code = ''
    domain_info = tldextract.extract(url)
    # print(domain_info)
    if domain_info.domain:
        if is_ip(domain_info.domain):
            host_code = domain_info.domain
        elif domain_info.suffix:
            host_code = f"{domain_info.subdomain}.{domain_info.domain}.{domain_info.suffix}"
            if host_code.find('%') > -1:
                host_code = ''
    return host_code.strip('.')


def is_ip(_str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(_str):
        return True
    else:
        return False


def filter_punctuation(input_str):
    """
    过滤标点符号
    :param input_str:
    :return:
    """
    re_punctuation = re.compile("[`~!@$^&*()=|｜{}':;',\\[\\].《》<>»/?~！@￥……&*（）——|{}【】‘；：”“'\"。，、？%+_]")
    result = re_punctuation.sub('', input_str)
    result = result.strip()
    return result


def match_url(input_str):
    """
    匹配url，规范输出
    :param input_str:
    :return:
    """
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    # 匹配模式
    url = re.findall(pattern, input_str)
    try:
        result = url[0]
    except Exception as e:
        result = ''
    return result


def is_need_filter(title=None, listpage_url=None, is_filter_reject_domain=False):
    status = None
    score = 0
    # title = title.lower()
    listpage_url = listpage_url.lower()

    # 标题长度过滤
    if len(title) < 2:
        status = 'title too short'
        return status, score
    if len(title) > 5:
        status = 'title too long'
        return status, score

    # URL长度过滤
    if len(listpage_url) < 10:
        status = 'URL too short'
        return status, score
    if len(listpage_url) > 150:
        status = 'URL too long'
        return status, score

    # host长度过滤
    host_code = get_host_code(listpage_url)
    if len(host_code) < 6:
        status = 'host_code too short'
        return status, score
    if len(host_code) > 40:
        status = 'host_code too long'
        return status, score
    if '···' in host_code:
        status = 'host_code illegal'
        return status, score

    # url ‘&’ 个数大于5过滤
    delimiter_count = listpage_url.count('&')
    if delimiter_count >= 5:
        status = 'too many &'
        return status, score

    # url没有http
    if 'http' not in listpage_url:
        status = 'not include http'
        return status, score

    # title & url自定义垃圾词过滤
    str_source = title + listpage_url
    invalid_str_pattern = "|".join(custom_str_invalid.custom_str_invalid_list)
    invalid_str = re.findall(invalid_str_pattern, str_source)
    if len(invalid_str) > 0:
        status = 'invalid_str: ' + ''.join(invalid_str)
        return status, score

    # 垃圾词过滤
    junkword_pattern = "|".join(reject_junkword.reject_junkword_list)
    junkword_match = re.findall(junkword_pattern, title)
    if len(junkword_match) > 0:
        status = 'junkword_match: ' + ''.join(junkword_match)
        return status, score

    # 垃圾域名过滤,速度比较慢，适用于无限制爬虫
    if is_filter_reject_domain:
        reject_domain_pattern = "|".join(reject_domain.reject_domain_list)
        reject_domain_match = re.findall(reject_domain_pattern, listpage_url)
        if len(reject_domain_match) > 0:
            status = 'reject_domain_match: ' + ''.join(reject_domain_match)
            return status, score

    # 栏目评分，根据标题关键词
    score_keyword_pattern = "|".join(custom_keyword_score.custom_keyword_score_dict.keys())
    match_keyword = re.findall(score_keyword_pattern, title)
    score = 10
    for i in match_keyword:
        score = score + custom_keyword_score.custom_keyword_score_dict[i]
    if score > 100:
        score = 100

    return status, score


if __name__ == '__main__':
    _title = '首页'
    _listpage_url = 'http://www.news.sohu.com/'

    status, level_score = is_need_filter(_title, _listpage_url, True)

    print(status, level_score)
    print(get_domain_code(_listpage_url))
    print(get_host_code(_listpage_url))


