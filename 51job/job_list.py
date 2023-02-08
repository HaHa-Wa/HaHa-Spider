# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/29 5:18 下午
@Auth ： HaHa-Wa
@File ：job_list.py
@IDE ：PyCharm
"""
import time
import hmac
from hashlib import sha256
import requests
from urllib.parse import urlencode

from pymongo import MongoClient

# 配置 mongodb参数
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = '51job'
MONGODB_CNAME = 'post'


# 请求加密参数
def get_sign(bb, p_u):
    appsecret = bb.encode('utf-8')  # 秘钥
    data = p_u.encode('utf-8')  # 加密数据
    sign = hmac.new(appsecret, data, digestmod=sha256).hexdigest()
    return sign


# 采集信息
def get_info(code):
    page = 1
    while True:
        # 定义时间戳
        time_s = str(int(time.time()))
        # 设置请求参数
        params = {
            'api_key': '51job',
            'timestamp': time_s,
            'keyword': 'python',
            'searchType': '2',
            'function': '',
            'industry': '',
            'jobArea': code,
            'jobArea2': '',
            'landmark': '',
            'metro': '',
            'salary': '',
            'workYear': '',
            'degree': '',
            'companyType': '',
            'companySize': '',
            'jobType': '',
            'issueDate': '',
            'sortType': '0',
            'pageNum': str(page),
            'requestId': '50975fe949fecb99ccf681d8b95c2cb6',
            'pageSize': '500',
            'source': '1',
            'accountId': '218864841',
            'pageCode': 'sou|sou|soulb',
        }
        # 拼接加密参数
        p_u = '/open/noauth/search-pc?' + urlencode(params)

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'From-Domain': '51job_web',
            'Origin': 'https://we.51job.com',
            'Pragma': 'no-cache',
            'Referer': 'https://we.51job.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'account-id': '218864841',
            'partner': '',
            'property': '%7B%22partner%22%3A%22%22%2C%22webId%22%3A2%2C%22fromdomain%22%3A%2251job_web%22%2C%22frompageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2F%22%2C%22pageUrl%22%3A%22https%3A%2F%2Fwe.51job.com%2Fpc%2Fsearch%3Fkeyword%3D%25E5%25A4%25A7%25E6%2595%25B0%25E6%258D%25AE%26searchType%3D2%26sortType%3D0%26metro%3D%22%2C%22identityType%22%3A%22%22%2C%22userType%22%3A%22%22%2C%22isLogin%22%3A%22%E6%98%AF%22%2C%22accountid%22%3A%22218864841%22%7D',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sign': get_sign(bb, p_u),
            'user-token': 'cea9af6467665e98ca3371bc8c9d5c18637d8746',
            'uuid': '45576bde9b1521fa60e855399bdb43d3',
        }

        url = 'https://cupid.51job.com/open/noauth/search-pc'
        # 发送请求
        response = requests.get(url, headers=headers, params=params)
        response.close()
        # 解析响应的json数据
        data = response.json()['resultbody']['job']['items']

        for x in data:
            print(x)
            # 将数据插入mongo
            insert_mongo(x)
        # 判断是否采集完毕
        if len(data) < 5000:
            break
        page += 1


def insert_mongo(item):
    data = dict(item)
    post.insert(data)
    return item


if __name__ == '__main__':
    # 加密 密钥
    bb = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'

    client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    mydb = client[MONGODB_DBNAME]
    post = mydb[MONGODB_CNAME]
    # 要采集的采集城市编码
    city_code = ['030200,040000,030800']
    for code in city_code:
        get_info(code)
    # 关闭mongo链接
    client.close()
