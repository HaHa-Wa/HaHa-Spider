# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/10 10:26 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import time
import os
import requests
import pandas as pd

type_dict = {
    '01010503': '年报',
    '012399': '特别退市整理期',
    '012399': '特别退市整理期',
    '012399': '特别退市整理期',
    '012399': '特别退市整理期',
    '012399': '特别退市整理期',
    '012399': '特别退市整理期',
}
Section = {
    ''
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def data_to_csv(data, file_name):
    df = pd.DataFrame(data)
    df.to_csv(file_name, encoding='utf-8')


def download_pdf(adjunctUrl, file_name):
    if not os.path.exists('pdf_file'):
        # 如果不存在则创建目录
        os.makedirs('pdf_file')
    file = requests.get(url=adjunctUrl, headers=headers)
    file_path = 'pdf_file/' + file_name
    with open(file_path, 'ab')as f:
        f.write(file.content)


def parse_info(announcements):
    data_onepage = []
    for announcement in announcements:
        secCode = announcement['secCode']
        secName = announcement['secName']
        announcementTitle = announcement['announcementTitle']
        announcementTime = announcement['announcementTime']
        announcementTime = time.localtime(announcementTime / 1000)
        announcementTime = time.strftime("%Y-%m-%d", announcementTime)
        announcementType = announcement['announcementType']
        announcementId = announcement['announcementId']
        pageColumn = announcement['pageColumn']
        adjunctUrl = announcement['adjunctUrl']
        adjunctUrl = 'http://static.cninfo.com.cn/' + adjunctUrl

        if d_pdf:
            file_name = adjunctUrl.split('/')[-1]
            print(file_name)
            download_pdf(adjunctUrl, file_name)
        data_onepage.append(
            [secCode, secName, pageColumn, announcementTitle, announcementTime, announcementId, adjunctUrl])
    return data_onepage


def get_info(data):
    all_info = [['代码', '简称', '板块', '公告标题', '公告时间', '公告ID', 'PDF链接']]

    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    res = requests.post(url, headers=headers, data=data)
    json_res = json.loads(res.content.decode())
    announcements = json_res['announcements']
    print(len(announcements))
    data_onepage = parse_info(announcements)
    all_info.extend(data_onepage)

    totalpages = json_res['totalpages']
    totalRecordNum = json_res['totalRecordNum']
    hasMore = json_res['hasMore']
    data_to_csv(all_info, 'test.csv')


def main():
    data = {
        "pageNum": 1,
        "pageSize": 30,
        'column': 'szse',
        'tabName': "fulltext",
        'plate': "",
        'stock': "",
        'searchkey': "",
        'secid': "",
        'category': "",
        'trade': "",
        'seDate': "{0}~{1}".format(start_time, end_time),
        'sortName': "",
        'sortType': "",
        'isHLtitle': "true"
    }
    get_info(data)


if __name__ == '__main__':
    d_pdf = False
    start_time = '2010-01-01'
    end_time = '2013-01-01'
    main()
