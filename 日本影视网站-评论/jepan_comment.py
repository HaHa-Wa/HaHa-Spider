# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/22 10:16 上午
@Auth ： HaHa-Wa
@File ：jepan_comment.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from retrying import retry


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_req(url):
    ret = requests.get(url, headers=headers, timeout=3)
    return ret


def get_list(mv_name, href):
    page = 1
    while True:
        url = 'https://filmarks.com{0}?page={1}'.format(href, page)

        ret = send_req(url)
        res = BeautifulSoup(ret.text, 'lxml')
        c_div = res.find('div', class_='p-main-area p-timeline')
        p_mark = c_div.find_all('div', class_='p-mark')
        for x in p_mark:
            name = x.find('h4', class_='c-media__text').text
            data_time = x.find('time', class_='c-media__date')['datetime']
            score = x.find('div', class_='c-rating__score').text
            content = x.find('div', class_='p-mark__review').text.strip()
            print(name, data_time, score, content)
            all_info.append([mv_name, href, name, data_time, score, content])
        if len(p_mark) != 10:
            break
        page += 1


def main():
    res = requests.get('https://filmarks.com/people/25190', headers)
    bs_res = BeautifulSoup(res.text, 'lxml')
    m_div = bs_res.find('div', class_='p-contents-grid')
    items = m_div.find_all('div', class_='c-content-item')
    h = False
    for item in items:
        h3 = item.find('h3', class_='c-content-item__title').find('a')
        mv_name = h3.text
        href = h3['href']
        print(href)
        if href == '/movies/32996':
            h = True
        if h:
            get_list(mv_name, href)


#     '/movies/6928'

if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    hea = ['电影名称', '链接', '评论人', '评论时间', '评分', '内容']
    all_info = [hea]
    try:
        main()
    except:
        print('出错了')
    df = pd.DataFrame(all_info)
    df.to_excel('mv3.xlsx')
