# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/8 10:02 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_list():
    all_info = []
    params = {
        'JournalID': '1',
        'query': 'شينجيانغ',
    }

    response = requests.get('https://akhbarelyom.com/News/Search/1/1', params=params, headers=headers)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    news_item = bs_ret.find_all('div', class_='entry-block-small')
    for item in news_item:
        # print(item)
        h2_a = item.find('h4').find('a')
        title = h2_a['title']
        href = 'https://akhbarelyom.com' + h2_a['href']
        # date_time = item.find('p', class_='bref').text
        print(title)
        print(href)
        detail, date_time = get_detail(href)
        all_info.append([title, date_time, detail, href])
    LastID = bs_ret.find('p', class_='lastid')['idx']

    for page in range(1, 4):
        print(page)
        params = {
            'JournalID': '1',
            'LastID': LastID,
            'query': 'شينجيانغ',
            '_': '1675842497773',
        }

        response = requests.get('https://akhbarelyom.com/News/SearchPaging', params=params, headers=headers)
        bs_ret = BeautifulSoup(response.text, 'lxml')
        news_item = bs_ret.find_all('div', class_='entry-block-small')
        for item in news_item:
            # print(item)
            h2_a = item.find('h4').find('a')
            title = h2_a['title']
            href = 'https://akhbarelyom.com' + h2_a['href']
            # date_time = item.find('p', class_='bref').text
            print('title:',title)
            print(href)
            detail,date_time = get_detail(href)

            all_info.append([title, date_time, detail, href])
        LastID = bs_ret.find('p', class_='lastid')['idx']

    df = pd.DataFrame(all_info)
    df.to_excel('akhbarelyom.xlsx')


def get_detail(href):
    response = requests.post(url=href, headers=headers)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    articleBody = bs_ret.find('div', class_='entry-content HtmlDecode')
    date_time = bs_ret.find('div', class_='post-meta-date').text
    print(articleBody.text)
    return articleBody.text, date_time


if __name__ == '__main__':

    headers = {
        'authority': 'akhbarelyom.com',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'html/text',
        'cookie': '_gid=GA1.2.1948134860.1675842177; __asc=343cb57d1862ffa67716f8c1966; __auc=343cb57d1862ffa67716f8c1966; __gads=ID=0acc1aa97465ecb6:T=1675842205:S=ALNI_MZujiVE5p4F_fb3BwkxEl6fsT3nmg; __gpi=UID=00000bb7c04d46ab:T=1675842205:RT=1675842205:S=ALNI_MaBe1x-f7-Vwa0EWUhCtJow08ceVw; _ga_WS3Q2CBBQQ=GS1.1.1675842176.1.0.1675842205.0.0.0; cto_bundle=MfOqJl9yNVRhYW5OaG9DOWRCc3piZnllUGVZVXBVYTVTaiUyQjRJQVQ0RWYyQVFKZ2d5dSUyRjhNJTJGQVl3OTVMZVJDd1I3MEk0SHR4QnhnVmFsN2ppa0NHNzJlbTRSS1ZmS0o1aTE1eXdYZ2lqQU5FYTFQSmZRTnkyZ2FZZlRTYkRwUExHS2VOd0RLbVVoTTFMOSUyRjRTSCUyQjFSJTJGWUpyT1Nwc0J3UjZtajdxQ1NXd3EwbHk3SHFjcDk5djhvQVR4NjJnSjVhbG5YMTNQUnZPJTJGT0QwRSUyQnhURFV6Z2dPdEJDdyUzRCUzRA; _ga_2FKKR3BH3S=GS1.1.1675842176.1.1.1675842497.54.0.0; _ga=GA1.2.235024384.1675842176; _gat_gtag_UA_57222535_1=1',
        'pragma': 'no-cache',
        'referer': 'https://akhbarelyom.com/News/Search/1/1?JournalID=1&query=%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    # get_detail()
    get_list()
