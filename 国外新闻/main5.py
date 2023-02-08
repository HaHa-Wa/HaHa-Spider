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
    for page in range(1, 75):
        print(page)
        response = requests.get(
            'https://www.mena.org.eg/search/quick/keywords/%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA/page/{0}'.format(page),
            headers=headers,
        )
        bs_ret = BeautifulSoup(response.text, 'lxml')
        news_item = bs_ret.find_all('ul', class_='MenaResultItem')
        for item in news_item:
            # print(item)
            h2_a = item.find('a')
            title = h2_a.text
            href = 'https://www.mena.org.eg'+h2_a['href']
            date_time = item.find('span', class_='MenaContentTimeStamp').text
            print(title)
            print(href)
            # detail = get_detail(href)

            all_info.append([title, date_time, href])
    df = pd.DataFrame(all_info)
    df.to_excel('mena.xlsx')


def get_detail(href):
    response = requests.post(url=href, headers=headers)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    articleBody = bs_ret.find('div', id='ContentPlaceHolder1_divContent')
    print(articleBody.text)
    return articleBody.text


if __name__ == '__main__':
    headers = {
        'authority': 'www.mena.org.eg',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': 'LanguageFront=ar; __utma=173448639.1410995111.1675842552.1675842552.1675842552.1; __utmc=173448639; __utmz=173448639.1675842552.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); AWSALB=89+lieiHB/owYJZ8GY4XPmAP+preP62A+NWZ02KQ+b1x0fh1mzBq8SQaOgVY2T668wKfMDcWmZnyma9LnI4vA30o/Mgc7m8YhE0AVaxFyzOkIAEN3H3l6S9vnRPU; AWSALBCORS=89+lieiHB/owYJZ8GY4XPmAP+preP62A+NWZ02KQ+b1x0fh1mzBq8SQaOgVY2T668wKfMDcWmZnyma9LnI4vA30o/Mgc7m8YhE0AVaxFyzOkIAEN3H3l6S9vnRPU; __utmb=173448639.5.10.1675842552',
        'pragma': 'no-cache',
        'referer': 'https://www.mena.org.eg/search/quick/keywords/%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA/page/25',
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
