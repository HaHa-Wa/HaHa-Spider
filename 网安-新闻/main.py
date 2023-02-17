# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/17 9:06 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import time

import pandas as pd
import requests
from lxml import etree
from retrying import retry

cookies = {
    'Hm_lvt_aafa9a8d6e1d47c37e7d21ba4f65619e': '1676541072',
    'XSRF-TOKEN': 'eyJpdiI6Imo1LzBuUy9WTWdqQUdxODJsMG53cUE9PSIsInZhbHVlIjoiaEMwNXNuK1pjVWoyL0xJQnJPY1hZTW5LWVRZOUh2Vk5yV1NkeFRpNW9wQTNRQzlhV3RyRHMvbk1EcGszU1FVbkpzZkpYUDdJK3dzWHVkYVNnN2ZYVDdicVA0KzlPOHpmNEp2bDhvTTVlZDIrY3pUdmZkdnVaUzFaN2xWMkM0UFMiLCJtYWMiOiIzMDA1MWFhYTA3N2RmZjZiZTgwZTE0OWNkM2MyYjFmY2JjY2U3YWVjNmI1MTBjNTU3ZGU2Yjc0ZTIwNTg3NTU5IiwidGFnIjoiIn0%3D',
    'nsg_session_pro': 'mKZt16dSLQD3mrlnjSrqlYz6mastUqUx4Wg8QGtb',
    'Hm_lpvt_aafa9a8d6e1d47c37e7d21ba4f65619e': '1676597226',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_aafa9a8d6e1d47c37e7d21ba4f65619e=1676541072; XSRF-TOKEN=eyJpdiI6Imo1LzBuUy9WTWdqQUdxODJsMG53cUE9PSIsInZhbHVlIjoiaEMwNXNuK1pjVWoyL0xJQnJPY1hZTW5LWVRZOUh2Vk5yV1NkeFRpNW9wQTNRQzlhV3RyRHMvbk1EcGszU1FVbkpzZkpYUDdJK3dzWHVkYVNnN2ZYVDdicVA0KzlPOHpmNEp2bDhvTTVlZDIrY3pUdmZkdnVaUzFaN2xWMkM0UFMiLCJtYWMiOiIzMDA1MWFhYTA3N2RmZjZiZTgwZTE0OWNkM2MyYjFmY2JjY2U3YWVjNmI1MTBjNTU3ZGU2Yjc0ZTIwNTg3NTU5IiwidGFnIjoiIn0%3D; nsg_session_pro=mKZt16dSLQD3mrlnjSrqlYz6mastUqUx4Wg8QGtb; Hm_lpvt_aafa9a8d6e1d47c37e7d21ba4f65619e=1676597226',
    'Pragma': 'no-cache',
    'Referer': 'https://zhuanlan.wangan.com/s/?keyword=%E6%BC%8F%E6%B4%9E',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_detail(href):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    # 发送请求
    response = requests.get(href, headers)
    # 转换html格式
    xp_res = etree.HTML(response.text)
    origin = xp_res.xpath('//p[@class="author-name"]/a/text()')[0]
    # 提取发布时间
    send_time = xp_res.xpath('//span[@class="article-published-at"]/text()')[1]
    # 提取发布内容
    content = xp_res.xpath("//div[@class='main-content article-container']//text()")
    # 拼接片段
    news = ''.join(content)
    print(send_time)
    return origin, send_time, news


def get_hot():
    s_time = '2021-06-09 10:12:55'
    while True:

        params = {
            'cursor': s_time,
            'page_size': '5',
        }
        # 发送请求
        response = requests.get('https://zhuanlan.wangan.com/data', params=params, cookies=cookies, headers=headers)
        # 提取json数据
        content = response.json()['data']['content']
        # 转换html格式
        ret = etree.HTML(content)
        # 提取所有新闻
        info = ret.xpath('//li')
        s_time = ret.xpath('//script/@data-max-value')[0]
        # print(s_time)
        # 便利新闻 提取详细字段
        for x in info:
            title = x.xpath('./a/text()')[0]
            href = x.xpath('./a/@href')[0]
            print(title, href)
            # 获取新闻详情
            origin, send_time, news = get_detail(href)
            # 添加进列表
            all_info.append([title, href, origin, send_time, news])
            # time.sleep(1)

        if len(info) != 5:
            break


if __name__ == '__main__':

    all_info = [['标题', '链接', '发布人', '发布时间', '新闻']]
    get_hot()
    # 列表转换喂excel
    df = pd.DataFrame(all_info)
    # 将数据写入excel
    with pd.ExcelWriter('店铺信息.xlsx', engine='xlsxwriter', options={'strings_to_urls': False}) as writer:
        df.to_excel(writer, index=False)
