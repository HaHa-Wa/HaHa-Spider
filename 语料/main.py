# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/25 11:10 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'authority': 'www.english-corpora.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'ASPSESSIONIDSGARSBAC=IFMHFPADKGKFMBGKAAFCLEDO; _ga=GA1.2.1591814170.1674548785; _gid=GA1.2.1738376695.1674548785; ASPSESSIONIDQEDQQCBC=IECODLNDAMKACNPOPOMJLJDO; password=; email=; ii=2',
    'pragma': 'no-cache',
    'referer': 'https://www.english-corpora.org/now/x3.asp?x2w=y&xx=1&w9=community&w10=of&w11=shared&w12=future&r=',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'frame',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def main():
    params = (
        ('node', ''),
        ('p', '2'),
        ('w9', 'community'),
        ('w10', 'of'),
        ('w11', 'shared'),
        ('w12', 'future'),
        ('r', ''),
    )

    response = requests.get('https://www.english-corpora.org/now/x3.asp', headers=headers, params=params)
    ret = response.content.decode()
    # print(ret)
    bs_ret = BeautifulSoup(ret, 'lxml')
    auto_style = bs_ret.find_all('table', class_='auto-style1')[1]
    trs = auto_style.find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        code = tds[0].text.strip()
        haha = tds[1].text.strip().split(' ')
        date_time = haha[0]
        com_href = tds[2].text.strip()
        detail_href = tds[2].find('a')['href']
        info = tds[9].text.strip()
        city = haha[1]
        print(code, date_time, com_href, info, city, '\n')
        # break
        year = date_time.split('-')[0]
        month = date_time.split('-')[1]
        one_info = [detail_href, com_href, year, month, city, info]
        all_info.append(one_info)


if __name__ == '__main__':
    # '文件名', '作者', '标题',
    all_info = [['网址', '新闻媒体', '年', '月', '国家', '内容']]
    main()
    df = pd.DataFrame(all_info)
    df.to_csv('test.csv')
