# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/12 3:47 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import os
import time

import requests
import pandas as pd
from bs4 import BeautifulSoup


def dowlound(zhuti, file_name, url):
    response = requests.get(
        url,
        headers=headers,
    )
    main_path = 'file/' + zhuti[:30].replace(':', '').replace('*', '') \
        .replace('/', '').replace('|', '').replace('\\', '').replace('<', '').replace('>', '')
    # \ / : * ? " < > |
    if not os.path.exists(main_path):
        os.mkdir(main_path)
    file_path = main_path + '/' + file_name
    with open(file_path, 'wb') as f:
        f.write(response.content)


def get_detail(zhuti, mail_id):
    # mail_id = 'ZL3507-mHLt2WksnOwN3wFiPrNeNde'
    response = requests.get(
        'https://exmail.qq.com/cgi-bin/readmail?folderid=1&t=readmail&mailid={0}&mode=pre&maxage=3600&base=10.6410&ver=14520&sid=vFbK1mYOxLRclEop,7&show_ww_icon=false'.format(
            mail_id),
        headers=headers,
    )
    ret = BeautifulSoup(response.text, 'lxml')
    contentDiv = ret.find('div', id='contentDiv')
    content = contentDiv.text
    data_time = ret.find('div', class_='receiver-inline-wrap').find('div', class_='cont tcolor').text
    try:
        receice_name = ret.find('span', class_='receiver-item-span').text
    except:
        receice_name = ''
    file_list = []
    name_bigs = ret.find_all('div', class_='name_big')
    for name_big in name_bigs:
        href = 'https://exmail.qq.com' + name_big.find('a')['href']

        file_name = name_big.find('span').text
        print(file_name, href)
        file_list.append([file_name, href])
        # dowlound(zhuti, file_name, href)
    return content, data_time, receice_name


def get_list():
    for page in range(0, int(page_)):
        print('page:', page)
        response = requests.get(
            'https://exmail.qq.com/cgi-bin/mail_list?sid=vFbK1mYOxLRclEop,7&page={0}&folderid=1&flag=&fun=&s=getmail&searchmode=&filetype=&listmode=&stype=&ftype=&AddrID=&grpid=&category=&showattachtag='.format(
                page),
            headers=headers,
        )
        ret = BeautifulSoup(response.text, 'lxml')
        toareas = ret.find_all('div', class_='toarea')
        for toarea in toareas:
            tables = toarea.find_all('table', class_='i M')
            for table in tables:
                # print(table)
                mail_id = table.find('input', {'name': 'mailid'})['value']
                send_name = table.find('td', class_='tl tf').text
                zhuti = table.find('td', class_='gt tf').find('u', class_='black').text
                send_time = table.find('td', class_='dt').text

                print(send_name, zhuti, send_time, '\n')
                content, data_time, receice_name = get_detail(zhuti, mail_id)
                all_info.append([send_name, receice_name, zhuti, data_time, content])


def time_date():
    time_local = time.localtime(time.time())
    # 转换成新的时间格式(精确到秒)
    dt = time.strftime("%Y-%m-%d %H-%M", time_local)
    return dt


if __name__ == '__main__':
    with open('cookie.txt', 'r', encoding='utf-8')as f:
        cookie = f.read()
    page_ = input('页码：')
    headers = {
        'authority': 'exmail.qq.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': cookie.replace('\n', ''),
        'pragma': 'no-cache',
        'referer': 'https://exmail.qq.com/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'iframe',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    all_info = [['发送人', '收件人', '主题', '发送时间', '正文']]
    get_list()
    df = pd.DataFrame(all_info)
    da_time = time_date()
    xlsx_name = '邮件数据' + da_time + '.xlsx'
    with pd.ExcelWriter(xlsx_name, engine='xlsxwriter', options={'strings_to_urls': False}) as writer:
        df.to_excel(writer, index=False)
