# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/9 12:44 上午
@Auth ： HaHa-Wa
@File ：douban.py
@IDE ：PyCharm
"""
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_list():
    for page in range(1, 5):
        print('page:', page)
        params = {
            'start': str(page * 50 - 50),
        }
        response = requests.get('https://www.douban.com/group/hellosleep/discussion', params=params,
                                headers=headers)
        ret = response.content.decode()
        bs_ret = BeautifulSoup(ret, 'lxml')
        olt = bs_ret.find('table', class_='olt')
        trs = olt.find_all('tr')
        for tr in trs[1:]:
            tit = tr.find('a')
            title = tit['title']
            href = tit['href']
            print(title, href)
            try:
                nickname, from_city, date_time, content = get_detail(href)
            except:
                continue
            all_info.append([title, href, nickname, from_city, date_time, content])
            time.sleep(1)


def get_detail(href):
    ret = requests.get(url=href, headers=headers)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    topic_doc = bs_ret.find('div', class_='topic-doc')
    nickname = topic_doc.find('span', class_='from').find('a').text
    from_city = topic_doc.find('span', class_='create-ip').text
    date_time = topic_doc.find('span', class_='create-time color-green').text
    content = topic_doc.find('div', class_='topic-content').text
    # print(nickname, from_city, date_time, content)
    return nickname, from_city, date_time, content


if __name__ == '__main__':

    all_info = []
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'll="118245"; bid=MEb8Eju-dm0; __utmc=30149280; __utmz=30149280.1675871396.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __yadk_uid=MvbwHC7f1rQYl0hzMzXLzCWlW0DxpwrB; __gads=ID=1f778844d77747bd-22ee510195d900ee:T=1675871402:RT=1675871402:S=ALNI_MbPD-tQEYjYTbQ0G9icaH5sW4mIYw; douban-fav-remind=1; dbcl2="267502782:8HZuCWfftZs"; ck=p19X; push_noty_num=0; push_doumail_num=0; __utmv=30149280.26750; _ga=GA1.2.791388715.1673683359; _gid=GA1.2.394026112.1675873736; frodotk_db="18c6c4a1d7edc43a4a544de587c94cae"; _ck_desktop_mode=1; vmode=pc; ct=y; __gpi=UID=00000bbe66177a48:T=1675871402:RT=1675903643:S=ALNI_MY-WqwhW1LKi89Pwr-pRbaSCZw6aA; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1675912570%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.791388715.1673683359.1675903643.1675912571.5; __utmt=1; _pk_id.100001.8cb4=1d0950420d661e48.1673683358.5.1675912579.1675904402.; __utmb=30149280.14.5.1675912579838',
        'Pragma': 'no-cache',
        'Referer': 'https://www.douban.com/group/hellosleep/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    try:
        get_list()
    except:
        print('出错了。。')
    # get_detail('https://www.douban.com/group/topic/279168349/')
    df = pd.DataFrame(all_info)
    df.to_excel('info2.xlsx')
