# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/17 11:37 上午
@Auth ： HaHa-Wa
@File ：search.py
@IDE ：PyCharm
"""
import requests
import pandas as pd
from lxml import etree
from retrying import retry

headers = {
    'authority': 'www.wangan.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'Hm_lvt_aafa9a8d6e1d47c37e7d21ba4f65619e=1676541072; XSRF-TOKEN=eyJpdiI6Imo1LzBuUy9WTWdqQUdxODJsMG53cUE9PSIsInZhbHVlIjoiaEMwNXNuK1pjVWoyL0xJQnJPY1hZTW5LWVRZOUh2Vk5yV1NkeFRpNW9wQTNRQzlhV3RyRHMvbk1EcGszU1FVbkpzZkpYUDdJK3dzWHVkYVNnN2ZYVDdicVA0KzlPOHpmNEp2bDhvTTVlZDIrY3pUdmZkdnVaUzFaN2xWMkM0UFMiLCJtYWMiOiIzMDA1MWFhYTA3N2RmZjZiZTgwZTE0OWNkM2MyYjFmY2JjY2U3YWVjNmI1MTBjNTU3ZGU2Yjc0ZTIwNTg3NTU5IiwidGFnIjoiIn0%3D; nsg_session_pro=mKZt16dSLQD3mrlnjSrqlYz6mastUqUx4Wg8QGtb; Hm_lpvt_aafa9a8d6e1d47c37e7d21ba4f65619e=1676601898; acw_tc=6f06f39716766049978896917e2d9a6ec6ef9fd6886d2c39f3fdd1b9b7; XSRF-TOKEN=eyJpdiI6IkZFNjE3cG9zWGUySzIzU3VsWFpoYmc9PSIsInZhbHVlIjoiNHFwdnZ2NzBKVWJ5RGxvSWNIa3VPUnNUa1dQNnJXWjgzaUZ1NEk4MjJIdy9mWng4TVBEOUhwZlBDeWtkbnJYSXV6RWtCa3plOXArQlBWUm92QlM1a3NWT3hKVUxjNHlFbEhxTEZtMitqMUlaM2t3bXBKSzFoUldWNkllN0hsOVUiLCJtYWMiOiIwYjg4MTJlZjY5ODhlNWE1MjU5OGRhY2VmZmQ0ZTMwYjMzYzhiMDU5MTAyZGNjZGE1YzZmNDAxZTM2YjkwMDcxIiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IjBaMlh3U1BpTlY2YWsvcWFrK3BHMmc9PSIsInZhbHVlIjoiZGQ4MDVmOHVxOVRZNnhWUlhGbWJwMWRZa2ttcGJ2NzQ0RU9nblJZajhxUjBSem1VOThVNVJxV0hPMzhRRk16MDVkaFlnTURkTDZ6Sm13ay96YTlGeTdPTmJaQ3NPeHBadHA1YnQ5UzJpQ2ZiWnkwN1ZiZEdDYi9uN200TXJoTDYiLCJtYWMiOiIwNjhiNWNlZWY4YWNmY2Q5NGYyNjZhNGQ1NzdjYWE5Mzk0ZjRmOTE4Nzc4YTI2Y2ZhNTc2NDJjOTcyNmMyZTFiIiwidGFnIjoiIn0%3D',
    'pragma': 'no-cache',
    'referer': 'https://www.wangan.com/s/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_detail(href):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    response = requests.get(href, headers)
    xp_res = etree.HTML(response.text)
    # 根据不同页面结构使用不同的 xpath
    try:
        origin = xp_res.xpath('//a[@class="article-author"]/text()')[0]
        send_time = xp_res.xpath('//span[@class="article-published-at"]/text()')[0]
    except:
        try:
            origin = xp_res.xpath('//p[@class="author-name"]/a/text()')[0]
            send_time = xp_res.xpath('//span[@class="article-published-at"]/text()')[1]
        except:
            origin = ''
            send_time =xp_res.xpath('//div[@class="article-infos"]/text()')[0]
    try:
        content = xp_res.xpath("//div[@class='main-content article-container']//text()")
    except:
        content = xp_res.xpath("div[@class='article-content js-article-content']//text()")
    news = ''.join(content)
    # print(send_time)
    return origin, send_time, news


def get_list():
    cursor = 55
    while True:
        print('cursor:', cursor)
        # 定义请求参数
        params = {
            'keyword': '网络安全',
            'cursor': str(cursor),
        }
        url = 'https://www.wangan.com/s/article/data'
        # 发送请求
        response = requests.get(url, params=params, headers=headers)
        # 提取json数据
        content = response.json()['data']['content']
        # 转换为xpath对象
        ret = etree.HTML(content)
        info = ret.xpath('//li')
        # 便利所有新闻
        for x in info:
            title = x.xpath('./a/text()')[0]
            href = x.xpath('./a/@href')[0]
            print(title, href)
            # try:
            if 'wenda' in href:
                continue
            try:
                # 提取新闻详情
                origin, send_time, news = get_detail(href)
            except:
                continue

            all_info.append([title, href, origin, send_time, news])
        print(len(info))
        if len(info) != 30:
            break
        cursor += 1


if __name__ == '__main__':
    all_info = [['标题', '链接', '发布人', '发布时间', '新闻']]
    try:
        get_list()
    except:
        print('出错了。。。')
    # 将数据写入excel
    df = pd.DataFrame(all_info)
    with pd.ExcelWriter('网络安全2.xlsx', engine='xlsxwriter', options={'strings_to_urls': False}) as writer:
        df.to_excel(writer, index=False)
