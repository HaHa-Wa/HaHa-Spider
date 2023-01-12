# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/11 5:31 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import os
import time

import requests

headers = {
    'authority': 'www1.hkexnews.hk',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'referer': 'https://www1.hkexnews.hk/search/titlesearch.xhtml?lang=zh',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


# 下载文件
def download(href, file_name):
    file = requests.get(url=href, headers=headers)

    with open('pdf_file2/%s' % file_name, 'ab')as f:
        f.write(file.content)


def main():
    haha = True
    params = {
        'sortDir': '0',
        'sortByOptions': 'DateTime',
        'category': '0',
        'market': 'SEHK',
        'stockId': '-1',
        'documentType': '-1',
        'fromDate': '20220101',
        'toDate': '20230101',
        'title': '',
        'searchType': '1',
        't1code': '40000',
        't2Gcode': '-2',
        't2code': '40400',
        'rowRange': '2400',
        'lang': 'zh',
    }
    url = 'https://www1.hkexnews.hk/search/titleSearchServlet.do'
    response = requests.get(url, params=params, headers=headers)
    res = json.loads(response.content.decode())['result']
    json_res = json.loads(res)
    print(len(json_res))
    if not os.path.exists('pdf_file2'):
        # 如果不存在则创建目录
        os.makedirs('pdf_file2')
    for info in json_res:
        STOCK_NAME = info['STOCK_NAME']
        TITLE = info['TITLE']
        FILE_LINK = 'https://www1.hkexnews.hk' + info['FILE_LINK']
        DATE_TIME = info['DATE_TIME'].replace('/', '-')
        STOCK_CODE = info['STOCK_CODE']
        timeArray = time.strptime(DATE_TIME, "%d-%m-%Y %H:%M")
        timestamp = time.mktime(timeArray)
        if len(TITLE) > 20:
            TITLE = TITLE[1: 20]
        if len(STOCK_NAME) > 20:
            STOCK_NAME = STOCK_NAME[1: 20]

        file_name = str(timestamp).replace('.0', '') + ' ' + DATE_TIME + STOCK_NAME + STOCK_CODE + '-' + TITLE.replace('/', '-') + '.pdf'
        print(FILE_LINK, '\n')
        file_name = file_name.replace('<br/>', '')
        print(file_name)
        if haha:
            download(FILE_LINK, file_name)
        if file_name == '滇池水務-2021 年度報告.pdf':
            haha = True


if __name__ == '__main__':
    main()
