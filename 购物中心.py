# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/21 11:27 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import re

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed
import pandas as pd
from retrying import retry


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_req(url):
    res_str = requests.get(url, headers=headers, timeout=3)
    assert res_str.status_code == 200
    return res_str


def ys_request(url):
    # 等一会2s
    res_str = send_req(url)

    soup = BeautifulSoup(res_str.text, 'html.parser')
    items = soup.find('ul', class_='l-list clearfix').find_all('li', class_='item')
    for item in items:
        href = item.find('h3', class_='fl l-name-h3').a['href']
        name = item.find('h3', class_='fl l-name-h3').a.string
        if name == '上海新邻生活站' or name == '上海缤谷文化休闲广场一期' or name == '上海花都荟购物广场':
            continue
        if 'http' not in href:
            continue
        print(href, name)
        get_detail_data(href, name)


# 获取明细数据 如开发商，项目信息
def get_detail_data(href, name):
    url = href
    id = name
    res_str = send_req(url)

    soup = BeautifulSoup(res_str.text, 'lxml')
    # 招商状态
    try:
        gd_Lng = re.findall('gd_Lng:(.*?),', res_str.text)[0]
        gd_Lat = re.findall('gd_Lat:(.*?),', res_str.text)[0]
        print(gd_Lng, gd_Lat)
        hh = soup.find_all('div', class_='detail-three-tit')
        # 开业状态
        # try:
        project_status = hh[0].text
        business_status = hh[1].text
        print(project_status, business_status)
        dict_jo = {'名称': id, 'is_success': True, '开业状态': project_status, '招商状态': business_status}
        attrs = soup.find('ul', class_='detail-option border-b').find_all('li')
        for attr in attrs:
            key = attr.find('span', class_='detail-option-name').text
            value = attr.find('span', class_='detail-option-value').text
            dict_jo[key] = value
        dict_jo['gd_Lng'] = gd_Lng
        dict_jo['gd_Lat'] = gd_Lat
        print(dict_jo)
        all_info.append(dict_jo)
    except:
        pass


# 根据链接获取列表数据
def list_data():
    url = 'http://bizsearch.winshangdata.com/xiangmu/s309-c0-t2019-r0-g0-x0-d0-z0-n0-m0-l0-q0-b0-y0-pn{0}.html'
    for i in range(2, 8):
        print('page:', i)
        request_url = url.format(i)
        ys_request(request_url)
    print('-------->finished')


def main():
    # 1.列表数据
    list_data()


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    title = ['名称', '开业时间', '面积', '开发商', '是否上市', '城市', '地址', '楼层', '项目状态', '项目类型', '招商状态']
    all_info = []
    try:
        main()
    except:
        print('出错了')
    df = pd.DataFrame(all_info)
    df.to_excel('上海购物中心3.xlsx')
