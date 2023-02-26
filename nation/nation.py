# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/25 9:31 下午
@Auth ： HaHa-Wa
@File ：nation.py
@IDE ：PyCharm
"""
import concurrent.futures

import requests
import retrying
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


@retrying.retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_q(url):
    ret = requests.get(url, headers=headers, timeout=3)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    return bs_ret


def get_detail(url):
    bs_ret = send_q(url)
    a_div = bs_ret.find('div', class_='article-content xxx')
    con_div = a_div.find('div', class_='col-1-1').text.strip().replace('\n\n', '')
    return con_div


def get_list(page):
    url = 'https://nation.africa/service/search/kenya/290754?pageNum={0}&query=Chinese&sortByDate=true'.format(page)

    bs_ret = send_q(url)
    search_result = bs_ret.find_all('li', class_='search-result')
    for li in search_result:
        a_html = li.find('a')
        href = 'https://nation.africa' + a_html['href']
        title = a_html['aria-label']
        article = a_html.find('article')
        author = article.find('span', class_='article-topic article-metadata_topic').text
        date_time = a_html.find('span', class_='date').text
        print(title, author, date_time)
        print(href)
        con_div = get_detail(href)
        if ('China' in con_div) or ('Chinese' in con_div) or ('china' in con_div):
            info = title + '\n' + author + '  ' + date_time + '\n' + con_div + '\n' + '-' * 20 + '\n'
            with open('info.txt', 'a')as f:
                f.write(info)


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for page in range(6, 51):
            future = executor.submit(get_list, page)
            futures.append(future)
        concurrent.futures.wait(futures)
