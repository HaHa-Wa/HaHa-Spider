# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/11 6:25 下午
@Auth ： HaHa-Wa
@File ：test.py
@IDE ：PyCharm
"""
import datetime
import re

import requests
import pdfkit
import pandas as pd

from bs4 import BeautifulSoup


def get_birthday_by_id_card(id_card):
    """通过身份证号获取 出生日期
       返回：datetime.date(1959, 2, 8)
    """
    if len(id_card) == 15:
        birth_year = int(id_card[6:8]) + 1900
        birth_month = int(id_card[8:10])
        birth_day = int(id_card[10:12])
    else:
        birth_year = int(id_card[6:10])
        birth_month = int(id_card[10:12])
        birth_day = int(id_card[12:14])
    return datetime.date(birth_year, birth_month, birth_day)


def parse_info(res):
    table_1 = res.find('div', class_='table_1')
    hahaha = ''
    if table_1:
        tables = table_1.find_all('table')
        for i, table in enumerate(tables[1:]):
            str_table = str(table)
            # print(str_table)
            re_ret = re.findall('<td>(.*?)</td>', str_table)
            name = re_ret[0]
            great = re_ret[1]
            code = re_ret[2]
            try:
                date = re_ret[5]
            except:
                date = ''
            Certificate = ' '.join([name, great, code, date])
            hahaha += '工种%s：' % str(i + 1)
            hahaha += Certificate
            hahaha += '\n'
        print(hahaha)
        return hahaha
    else:
        return '无证书'


def get_info(name, code):
    cookies = {
        'JSESSIONID': '635048401D84067393BBB88F6B4D3883',
        'Hm_lvt_e85984af56dd04582a569a53719e397f': '1673432255',
        'Hm_lpvt_e85984af56dd04582a569a53719e397f': '1673432660',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        # 'Cookie': 'JSESSIONID=635048401D84067393BBB88F6B4D3883; Hm_lvt_e85984af56dd04582a569a53719e397f=1673432255; Hm_lpvt_e85984af56dd04582a569a53719e397f=1673432660',
        'Origin': 'http://zscx.osta.org.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://zscx.osta.org.cn/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    data = {
        'tableName': 'CERT_T',
        'tableName1': '000000',
        'CertificateID': '',
        'CID': code,
        'Name': name,
        'province': '-1',
        '__captchaVerification': 'EDJKqe3Tvv5V88LT2IyrQbQOBZf5nlR2foI8D3JUjkcZJPjprF4ao5gPtQLZzSnHsjvwdL3KdL8qo+RmM+UqxI8irfviC/zK3YCluaTVDGo=',
    }
    # 'CID': '42280119701101227X',
    # 'Name': '范锦文',
    response = requests.post(
        'http://zscx.osta.org.cn/jiandingApp/command/buzhongxin/ecCertSearchAll',
        cookies=cookies,
        headers=headers,
        data=data,
        verify=False,
    )
    res = response.text
    bs_res = BeautifulSoup(res, 'lxml')
    zscxsj = bs_res.find('div', id='center_jg')
    birth = str(get_birthday_by_id_card(code)).replace('-', '.')
    print(birth)

    hahaha = parse_info(zscxsj)
    if hahaha != '无证书':
        html = '<html><head><meta charset="UTF-8"></head>' \
               '<body><div align="left"><p>%s</p></div></body></html>' % zscxsj
        pdfkit.from_string(html, '技能人才评价证书查询/file2/%s.pdf' % name)
    # else:
    #     hahaha = '无证书'
    return hahaha, birth


def main():
    res = pd.read_excel('2022 大力总表.xlsx')
    for x in res.itertuples():
        name = x[2]
        code = x[3]
        if name != '姓名' and type(name) != float:
            print(x[2], x[3])
            print(type(code))

            print(name, code)
            zscxsj, birth = get_info(name, code)
            one_info = [name, code, zscxsj, birth]
            all_info.append(one_info)


def parse_csv():
    new_list = [['姓名', '身份证', '已有证书', '出生年月']]
    ret = pd.read_excel('技能人才查询-20230112.xlsx')
    for x in ret.itertuples():
        haha = x[4].replace('/高级技能', '').replace('/初级技能', '').replace('/中级技能', '')
        # print(haha)
        info = [x[2], x[3], haha, str(x[5]).replace(' 00:00:00', '')]
        print(info)
        new_list.append(info)
    df = pd.DataFrame(new_list)
    df.to_excel('技能人才评定-20230112-1.xlsx')


if __name__ == '__main__':
    all_info = [['姓名', '身份证', '已有证书', '出生年月']]
    main()
    # parse_csv()
    df = pd.DataFrame(all_info)
    df.to_excel('技能人才评价证书查询-20230112-2.xlsx')
