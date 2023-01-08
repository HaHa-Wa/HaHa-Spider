# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/7 6:19 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import os
import random
import time

import pandas as pd
import requests
import re
from bs4 import BeautifulSoup


def get_industry(haha='制造业'):
    data = {
        'nodecode': '',
        'name': '',
        'hyids': ''
    }

    response = requests.post(
        'http://permit.mee.gov.cn/perxxgkinfo/common/tree/xzxk-common-trade!hynodeslist.action',
        headers=headers,
        data=json.dumps(data),
        verify=False,
    )

    ret = json.loads(response.text.replace('/**/', ''))
    parent_id = []
    name_list = []
    code_list = []
    for x in ret:
        if x['singlehyname'] == haha:
            parent_id.append(x['id'])
        if not x.get('pid'):
            if x['pId'] in parent_id:
                if not x['isParent']:
                    name_list.append(x['singlehyname'])
                    code_list.append(x['id'])
                    # isParent_list.append([x['id'], x['singlehyname']])
                else:
                    parent_id.append(x['id'])
    print(parent_id)

    treadname = ','.join(name_list)
    treadcode = ','.join(code_list)
    return treadname, treadcode


def getcity(parentCode):
    data = {
        'parentCode': parentCode
    }

    response = requests.post(
        'http://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!getRegions.action',
        headers=headers,
        data=data,
    )
    city_ret = json.loads(response.text)['regions']
    # print(city_ret)
    return city_ret


def main(province_id, city_id):
    treadname, treadcode = get_industry(haha)
    print(treadname)
    data = {
        'page.pageNo': 2,
        'page.orderBy': '',
        'page.order': '',
        'tempReportKey': 'd748801980b748a3aa37b573903e894f',
        'province': province_id,
        'city': city_id,
        'registerentername': '',
        'xkznum': '',
        'treadname': treadname,
        'treadcode': treadcode,
        'publishtime': ''
    }
    url = 'http://permit.mee.gov.cn/perxxgkinfo/syssb/xkgg/xkgg!licenseInformation.action'
    page = 1
    tempReportKey = 'd748801980b748a3aa37b573903e894f'
    all_info = [['省/直辖市', '地市', '许可证编号', '单位名称', '行业类别', '有效期限', '发证日期']]

    while True:
        # for page in range
        data['page.pageNo'] = page
        data['tempReportKey'] = tempReportKey
        response = requests.post(url, headers=headers, data=data)
        res = BeautifulSoup(response.text, 'lxml')
        tb_con = res.find('div', class_='tb-con')
        trs = tb_con.find_all('tr')
        tempReportKey = re.findall(r'name="tempReportKey"  value="(.*?)"', response.text)[0]
        try:
            page_max = re.findall(r'共(.*?)页', response.text)[0]
        except:
            print('没有数据')
            break
        for tr in trs[1:]:
            tds = tr.find_all('td')
            province = tds[0].text
            city = tds[1].text
            code = tds[2].text
            unit_name = tds[3].text
            industry_category = tds[4].text
            validity_period = tds[5].text
            date_of_issue = tds[6].text
            all_info.append([
                province, city, code, unit_name, industry_category, validity_period, date_of_issue
            ])
        print('正在采集第%s页。。' % page)
        if page == int(page_max):
            break
        page += 1
        time.sleep(random.randint(1, 2))

    if not os.path.exists('output'):
        os.mkdir('output')
    df = pd.DataFrame(all_info)
    file_name = province_name + haha + '.csv'
    df.to_csv('output/%s' % file_name)


if __name__ == '__main__':
    headers = {
        "Cookie": "JSESSIONID=D2775394C92345C5FAD9DA6B9277F780; paiwu80_cookie=45380249",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    haha = input('输入行业：')
    parentCode = '000000000000'
    regions = getcity(parentCode)

    province_name = input('输入省份：')
    if province_name == '':
        province_id = ''
        city_id = ''
    else:
        for x in regions:
            if x['regionname'] == province_name:
                province_id = x['regioncode']
        city_info = getcity(str(province_id))
        for x in city_info:
            print(x['regionname'], x['regioncode'])
        city_id = input('输入城市ID：')
    main(province_id, city_id)
