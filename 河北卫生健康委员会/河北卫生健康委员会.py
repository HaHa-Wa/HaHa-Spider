# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/2 8:58 下午
@Auth ： HaHa-Wa
@File ：河北卫生健康委员会.py
@IDE ：PyCharm
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup
from retrying import retry

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Pragma': 'no-cache',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://wsjkw.hebei.gov.cn/html/yqtb/index.jhtml',
    'Upgrade-Insecure-Requests': '1',
    "Cookie": "_site_id_cookie=1; JSESSIONID=C028F871DA257EEA48559E8C6339955A",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def detail(url):
    # url = 'http://wsjkw.hebei.gov.cn/yqtb/391924.jhtml'
    # 发送请求
    ret = requests.get(url, headers, timeout=5)
    res = BeautifulSoup(ret.text, 'lxml')
    # 请求失败重新请求
    try:
        zoom = res.find('div', id='zoom').text
    except:
        ret = requests.get(url, headers)
        res = BeautifulSoup(ret.text, 'lxml')
        zoom = res.find('div', id='zoom').text
        print('href:', url)
    return zoom


# 请求失败重试
@retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_msg(url):
    # 发送请求
    response = requests.get(url, headers=headers, timeout=5)
    ret = response.text
    res = BeautifulSoup(ret, 'lxml')
    # 定位数据
    ul = res.find('ul', class_='er-list2')
    li_list = ul.find_all('li')
    return li_list


def main():
    for page in range(1, 90):
        url = 'http://wsjkw.hebei.gov.cn/html/yqtb/index_{0}.jhtml'.format(page)
        li_list = send_msg(url)

        for li in li_list:
            a = li.find('a')
            href = a['href']
            title = a.text
            date_time = li.find('span').text
            print(title, href)
            # 获取详情数据
            zoom = detail(href)
            all_info.append([
                title, href, date_time, zoom
            ])


if __name__ == '__main__':
    all_info = [['标题', '链接', '时间', '正文']]
    main()
    # 将数据写入excel
    # df = pd.DataFrame(all_info)
    # df.to_excel('news.xlsx')
