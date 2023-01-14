# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/14 3:13 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import requests
import pandas as pd

def main(area):
    url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode={0}&t=1673680319424'.format(area[0])
    headers = {
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    }
    res = requests.get(url, headers=headers)
    res = json.loads(res.text)
    data = res['data']['list']
    for info in data:
        today = info['today']
        date = info['date']
        if date[0:4] == '2022':
            print(today)
            all_info.append([str(info['date']), today['confirm'], today['heal'], today['dead']])


if __name__ == '__main__':
    areaCode = '420000'
    areaName = '湖北省'
    area_list = [['420000', '湖北省']]
    for area in area_list:

        all_info = [['日期', '确诊', '治愈', '死亡']]
        main(area)
        df = pd.DataFrame(all_info)
        df.to_excel('{0}.xlsx'.format(area[1]))
