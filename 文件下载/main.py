# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/5 2:52 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import time

import requests
from bs4 import BeautifulSoup


# 下载文件
def download(href, file_name):
    file = requests.get(url=href, headers=headers)
    if len(file.content) < 40165940:
        while True:
            file = requests.get(url=href, headers=headers)
            if len(file.content) > 40165940:
                break
            time.sleep(3)
    with open('file/%s' % file_name, 'ab')as f:
        f.write(file.content)


# 主流程
def main():
    # 设置请求链接
    URL = 'https://doi.pangaea.de/10.1594/PANGAEA.914912?format=html'
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    # 发起请求
    res = requests.get(url=URL, headers=headers)
    # 解析返回的html文本
    bs_ret = BeautifulSoup(res.content.decode(), 'lxml')
    # 定位到数据表格
    table = bs_ret.find('table', class_='dditable')
    # 定位到文件位置
    trs = table.find_all('tr')
    hh = False
    #
    for tr in trs[1:]:
        # 定位文件精确位置
        tds = tr.find_all('td')
        try:
            # 取出文件链接 及文件名
            a_info = tds[6].find('a')
            href = a_info['href']
            file_name = a_info.text
        except:
            continue
        # 输出文件链接 及 文件名
        print(href, file_name)
        # 下载文件
        download(href, file_name)
        break


if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    main()
