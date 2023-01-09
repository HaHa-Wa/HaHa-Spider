# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/5 5:15 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import requests
from bs4 import BeautifulSoup
from xml.etree.ElementTree import Element, ElementTree


def get_comment(docid):
    # 设置评论请求参数
    params = {
        'offset': '0',
        'limit': '10',
        'headLimit': '3',
        'tailLimit': '2',
        'ibc': 'newswap',
        'showLevelThreshold': '5',
        'callback': 'callback_1672935010153',
    }
    # 发送请求
    response = requests.get(
        'https://comment.api.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/%s/comments/newList' % docid,
        params=params,
        headers=headers,
    )
    # 接收返回结果
    res = response.text
    # 将结果转为json格式
    comment_list = json.loads(res[res.find('(') + 1: -1])
    comments = []
    # 取出评论 放入列表中
    for id, comment in comment_list['comments'].items():
        comments.append(comment['content'])
    print(comments)
    # 返回结果
    return comments


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
    root = Element('news')
    # 循环遍历多页采集
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
            doc = Element('doc')
            print(news)
            # 构建新闻URL
            detail_url = 'https://www.163.com/dy/article/%s.html' % news['docid']
            title = news['title']
            date = news['ptime']
            source = news['source']
            # 采集新闻详情
            Paragraphs = get_detail(detail_url)
            try:
                # 采集新闻评论
                comments = get_comment(news['docid'])
            except:
                continue
            haha = {
                'url': detail_url,
                'title': title,
                'date': date,
                'source': source,
                'Paragraphs': Paragraphs,
                # 'comments': comments
            }
            # 将数据放进xml文件
            for key, val in haha.items():
                child = Element(key)
                child.text = str(val)
                doc.append(child)
            # 将评论放入xml文件
            comment_xml = Element('comments')
            for x in comments:
                comment = Element('comment')
                comment.text = str(x)
                comment_xml.append(comment)
            doc.append(comment_xml)
            # 将单个新闻xml放入整体xml文件
            root.append(doc)
    # 保存xml文件
    tree = ElementTree(root)
    tree.write('result.xml', encoding='utf-8')


if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    main()
