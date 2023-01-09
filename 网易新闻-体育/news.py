# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/6 8:39 下午
@File ：news.py
@IDE ：PyCharm
"""
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_detail(url):
    print(url)
    # 发送请求
    res = requests.get(url, headers=headers)
    # 解析返回结果
    bs_ret = BeautifulSoup(res.text, 'lxml')
    # 定位文本内容
    post_body = bs_ret.find('div', class_='post_body')
    if not post_body:
        post_body = bs_ret.find('div', class_='article-details')
    return post_body.text


def main():
    # 构建xml文件
    # 循环遍历多页采集
    all_info = [['标题', '时间', '来源', '正文', '链接']]
    for page in range(1, 20):
        num = (page - 1) * 15
        # 设置url
        url = 'https://3g.163.com/touch/reconstruct/article/list/BA8E6OEOwangning/%s-15.html' % str(num)
        # 发送请求
        ret = requests.get(url=url, headers=headers)
        # 解析返回结果
        res_json = json.loads(ret.text.replace('artiList(', '')[:-1])
        # 将数据转换为json格式
        news_list = res_json['BA8E6OEOwangning']
        # 遍历新闻列表
        for news in news_list:
            # 构建单个新闻xml
            print(news)
            # 构建新闻URL
            detail_url = 'https://www.163.com/dy/article/%s.html' % news['docid']
            title = news['title']
            date = news['ptime']
            source = news['source']
            # 采集新闻详情
            Paragraphs = get_detail(detail_url)
            # 将新闻放入列表
            all_info.append([title, date, source, Paragraphs, detail_url])

    df = pd.DataFrame(all_info)
    df.to_excel('网易新闻-体育.xls')


if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    main()
