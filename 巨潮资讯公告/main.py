# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/11 12:03 下午
@Auth ： HaHa-Wa
@File ：test.py
@IDE ：PyCharm
"""
# coding: utf-8
import json
import time
import os
import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
ua = UserAgent()

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

TITLE = ['代码', '简称', '板块', '公告标题', '公告时间', '公告ID', 'PDF链接', '公告类型']


def data_to_csv(data, file_name):
    df = pd.DataFrame(data)
    df.to_csv(file_name, encoding='utf-8')


def download_pdf(adjunctUrl, file_name):
    if not os.path.exists('pdf_file'):
        # 如果不存在则创建目录
        os.makedirs('pdf_file')
    headers = {
        "User-Agent": ua.chrome
    }
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
        announcementType = str(announcement['announcementType'].split('||'))
        announcementId = announcement['announcementId']
        pageColumn = announcement['pageColumn']
        adjunctUrl = announcement['adjunctUrl']
        adjunctUrl = 'http://static.cninfo.com.cn/' + adjunctUrl

        if d_pdf:
            file_name = adjunctUrl.split('/')[-1]
            download_pdf(adjunctUrl, file_name)
        data_onepage.append(
            [secCode, secName, pageColumn, announcementTitle, announcementTime, announcementId, adjunctUrl,
             announcementType])
    return data_onepage


def get_info(data, page):
    print(data)
    data['pageNum'] = page
    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers = {
        "User-Agent": ua.chrome
    }
    res = requests.post(url, headers=headers, data=data)
    json_res = json.loads(res.content.decode())
    announcements = json_res['announcements']
    print('-' * 20)
    print(announcements)
    data_onepage = parse_info(announcements)
    all_info.extend(data_onepage)


def get_max_page(data):
    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers = {
        "User-Agent": ua.chrome
    }
    res = requests.post(url, headers=headers, data=data)
    json_res = json.loads(res.content.decode())
    totalpages = json_res['totalpages']
    return totalpages


if __name__ == '__main__':
    info_type = [
        {"key": "category_ndbg_szsh", "value": "年报"},
        {"key": "category_bndbg_szsh", "value": "半年报"},
        {"key": "category_yjdbg_szsh", "value": "一季报"},
        {"key": "category_sjdbg_szsh", "value": "三季报"},
        {"key": "category_yjygjxz_szsh", "value": "业绩预告"},
        {"key": "category_qyfpxzcs_szsh", "value": "权益分派"},
        {"key": "category_dshgg_szsh", "value": "董事会"},
        {"key": "category_jshgg_szsh", "value": "监事会"},
        {"key": "category_gddh_szsh", "value": "股东大会"},
        {"key": "category_rcjy_szsh", "value": "日常经营"},
        {"key": "category_gszl_szsh", "value": "公司治理"},
        {"key": "category_zj_szsh", "value": "中介报告"},
        {"key": "category_sf_szsh", "value": "首发"},
        {"key": "category_zf_szsh", "value": "增发"},
        {"key": "category_gqjl_szsh", "value": "股权激励"},
        {"key": "category_pg_szsh", "value": "配股"},
        {"key": "category_jj_szsh", "value": "解禁"},
        {"key": "category_gszq_szsh", "value": "公司债"},
        {"key": "category_kzzq_szsh", "value": "可转债"},
        {"key": "category_qtrz_szsh", "value": "其他融资"},
        {"key": "category_gqbd_szsh", "value": "股权变动"},
        {"key": "category_bcgz_szsh", "value": "补充更正"},
        {"key": "category_cqdq_szsh", "value": "澄清致歉"},
        {"key": "category_fxts_szsh", "value": "风险提示"},
        {"key": "category_tbclts_szsh", "value": "特别处理和退市"},
        {"key": "category_tszlq_szsh", "value": "退市整理期"}]
    d_pdf = False  # 需要保存PDF 则改为 True
    start_time = '2010-01-01'
    end_time = '2013-01-01'
    data = {
        "pageNum": 1,
        "pageSize": 30,
        'column': 'szse',
        'tabName': "fulltext",
        'plate': "",
        'stock': "300085,9900012331",
        'searchkey': "",
        'secid': "",
        'category': "",
        'trade': "",
        'seDate': "{0}~{1}".format(start_time, end_time),
        'sortName': "",
        'sortType': "",
        'isHLtitle': "true"
    }
    all_info = [TITLE]

    max_page = get_max_page(data)
    get_info(data, page=1)
    # with ThreadPoolExecutor(3) as t:
    #     for page in range(1, max_page):
    #         print(page)
    #         t.submit(get_info, data=data, page=page)  # 传入要执行的函数及其参数
    # file_name = start_time+' '+end_time +'.csv'
    # data_to_csv(all_info, file_name)
