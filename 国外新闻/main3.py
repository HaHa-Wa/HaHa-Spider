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
    for page in range(1, 5):
        print(page)
        params = {
            'StartRowIndex': str(20*page -20),
        }

        response = requests.get(
            'https://gate.ahram.org.eg/Search/%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA.aspx',
            params=params,
            headers=headers,

        )
        bs_ret = BeautifulSoup(response.text, 'lxml')
        news_item = bs_ret.find_all('div', class_='col-lg-12 d-flex border-m bg-contant-outer m-bottom')
        for item in news_item:
            # print(item)
            h2_a = item.find('a')
            title = h2_a.text
            href = h2_a['href']
            date_time = item.find('p', class_='bref').text
            print(title)
            print(href)
            detail = get_detail(href)

            all_info.append([title, date_time, detail, href])
    df = pd.DataFrame(all_info)
    df.to_excel('ahram.xlsx')


def get_detail(href):
    response = requests.post(url=href, headers=headers)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    articleBody = bs_ret.find('div', id='ContentPlaceHolder1_divContent')
    print(articleBody.text)
    return articleBody.text


if __name__ == '__main__':
    headers = {
        'authority': 'gate.ahram.org.eg',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': '__qca=P0-2063252014-1675820326829; ASP.NET_SessionId=2tde1cgn4ztrc3dlqtwg25p5; _ga=GA1.1.1097595107.1675820306; udmsrc=%7B%7D; _pbjs_userid_consent_data=3524755945110770; __qca=P0-2063252014-1675820326829; pbjs-unifiedid=%7B%22TDID%22%3A%22a4d11d2b-3a8e-4b66-98e6-dcfbe5d3bb19%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-01-08T01%3A38%3A51%22%7D; _ga_X3WCWTFPLM=GS1.1.1675828810.2.0.1675828810.0.0.0; __cf_bm=onFBSX58I7NgGLAU0sGD.OG2WhXTQR_vAX0oSWgGVVk-1675828820-0-AVTCtuuAgGkSiz41CENLo+gHhslgS3IwpbHewS4QXqWgxdIk/4Alt14WlPZ4EU+2SALQ6rPF+BehwwaYyPjh8yvq4iB4hdZqRyvbxGH5OG2kLDL97Tlu3ZZvqZMeq5xGs7mCjuPbQITetY78gTEADMY=; _ga_TL2EBYD9CQ=GS1.1.1675828818.2.0.1675828822.0.0.0; udm_edge_floater_fcap=%5B1675828824440%5D; udm_session=1; udm_session_rad=1; cto_bundle=5B_H-V80d2tlamxjbHNETjlXODhmQlcwMmowMVUlMkZ6WWsxaWswUGVtOU9adnAlMkY1aVpjVlptJTJGelRuaVV3c0UyeXExN3V1bVVNMWJGSTdQVUdta01qbHJ1SUxYV1UlMkZIQXlrbkJlSlZsTWxTJTJGT3lZdUg2d2hYc0NwQTdIV0tRYzlERUlLbHF0N0l6Z1Bjbm5EdzBjcEV5dTZZelVnJTNEJTNE',
        'pragma': 'no-cache',
        'referer': 'https://gate.ahram.org.eg/Search/%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA.aspx?Eid=',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    # get_detail()
    get_list()
