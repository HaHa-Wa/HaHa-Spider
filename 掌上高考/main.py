# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/10 1:07 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import time

import execjs
import requests
import pandas as pd
# from selenium import webdriver
from urllib.parse import urlparse

from bs4 import BeautifulSoup

with open('jm.js')as f:
    js_code = f.read()
jm_js = execjs.compile(js_code)

url = "https://api.eol.cn/gkcx/api/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/83.0.4103.97 Safari/537.36"
}
haha = False


def get_params(request_payload):
    """构造请求参数"""
    words = []
    for k, v in request_payload.items():
        _ = str(k) + "=" + str(v)
        words.append(_)
    # print(words)
    data = "&".join(words)
    # print(data)

    url_data = urlparse(url)

    params = url_data.netloc + url_data.path + "?" + data
    print(params)

    return params


def get_sign(param):
    """获取sign参数"""
    params = {"data": param}
    # url = jm_url + "get_sign"
    # sign = requests.get(url=url, params=params).text
    sign = jm_js.call('get_sign', params)
    print("sign", sign)
    return sign


def parse(html):
    bs_ret = BeautifulSoup(html, 'lxml')
    card = bs_ret.find('div', class_='schoolName clearfix school_view_top')
    line3_item = card.find_all('span', class_='school-info-label')
    try:
        wangzhi = line3_item[0].text
    except:
        wangzhi = ''
    try:
        dianhua = line3_item[1].text
    except:
        dianhua = ''
    try:
        youxiang = line3_item[2].text
    except:
        youxiang = ''
    print(wangzhi, dianhua, youxiang)
    spans = bs_ret.find_all('span', class_='ellipsis float_l')
    try:
        zhandi = spans[1].text
    except:
        zhandi = ''
    try:
        weizhi = spans[3].text
    except:
        weizhi = ''
    print(zhandi, weizhi)
    return wangzhi, dianhua, youxiang, zhandi, weizhi


def get_school_info(school_id):
    headers = {
        'authority': 'static-data.gaokao.cn',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'origin': 'https://m.gaokao.cn',
        'pragma': 'no-cache',
        'referer': 'https://m.gaokao.cn/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    }
    url = 'https://static-data.gaokao.cn/www/2.0/school/{0}/info.json'.format(school_id)
    response = requests.get(url, headers=headers)
    ret = response.json()['data']
    address = ret['address']
    email = ret['email']
    site = ret['site']
    school_site = ret['school_site']
    phone = ret['phone']

    dualclass = ret['dualclass']
    dualclass = ' '.join([x['class'] for x in dualclass])
    return address, email, site, school_site, phone, dualclass


def get_response(request_payload, sign):
    """获取xhr返回的数据"""
    # global haha
    request_payload["signsafe"] = sign
    response = requests.post(url=url, headers=headers, data=json.dumps(request_payload), params=request_payload)
    data = response.json()
    # print(data)
    data = data["data"]["item"]
    # print(data)
    for x in data:
        schoolId = x['school_id']
        # if schoolId == 3418:
        #     haha = True
        # if haha:
        href = 'https://www.gaokao.cn/school/' + str(schoolId)
        print(href)
        # drive.get(href)
        # time.sleep(2)
        # html = drive.page_source
        # wangzhi, dianhua, youxiang, zhandi, weizhi = parse(html)
        address, email, site, school_site, phone, dualclass = get_school_info(schoolId)
        x['address'] = address
        x['email'] = email
        x['site'] = site
        x['school_site'] = school_site
        x['phone'] = phone
        x['dualclass'] = dualclass
        x['logo'] = 'https://static-data.gaokao.cn/upload/logo/{0}.jpg'.format(schoolId)
        # x['wangzi'] = wangzhi.replace('官方网址：', '')
        # x['dianhua'] = dianhua.replace('官方电话：', '')
        # x['youxiang'] = youxiang.replace('电子邮箱：', '')
        # x['zhandi'] = zhandi.replace('学校地址：', '')
        # x['weizhi'] = weizhi.replace('占地面积（亩）：', '')
        all_info.append(x)
    return data


def main():
    request_payload = {
        'admissions': '',
        'central': '',
        'department': '',
        'dual_class': '',
        'f211': '',
        'f985': '',
        'is_doublehigh': '',
        'is_dual_class': '',
        'keyword': '',
        'nature': '',
        'page': 1,
        'province_id': '',
        'ranktype': '',
        'request_type': 1,
        'school_type': '',
        # 'signsafe': '08f9c20fc7ed497c62d97d3a7aabc600',
        'size': 20,
        'type': '',
        'uri': 'apidata/api/gk/school/lists',
    }
    for page in range(1, 142):
        request_payload['page'] = page
        param = get_params(request_payload)
        sign = get_sign(param)
        get_response(request_payload, sign)
        # break

if __name__ == '__main__':
    # drive = webdriver.Chrome()
    all_info = []
    # try:
    main()
    # except:
    print('出错了')
    df = pd.DataFrame(all_info)
    df.to_excel('schrool3.xlsx')

    # get_decrypt_data(response)
