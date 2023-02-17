# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/8 11:38 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import requests
import time
import pandas as pd

def main(id):
    cookies = {
        'uid': 'rB02iWPjpDCofmzMx3OrAg==',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218631395fb4e22-0f64390783d3e48-16525635-2007040-18631395fb5100b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2MzEzOTVmYjRlMjItMGY2NDM5MDc4M2QzZTQ4LTE2NTI1NjM1LTIwMDcwNDAtMTg2MzEzOTVmYjUxMDBiIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218631395fb4e22-0f64390783d3e48-16525635-2007040-18631395fb5100b%22%7D',
        '_ga': 'GA1.1.1291950143.1675863090',
        '_ga_9PQ283MLZQ': 'GS1.1.1675869151.2.1.1675870581.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': 'uid=rB02iWPjpDCofmzMx3OrAg==; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218631395fb4e22-0f64390783d3e48-16525635-2007040-18631395fb5100b%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2MzEzOTVmYjRlMjItMGY2NDM5MDc4M2QzZTQ4LTE2NTI1NjM1LTIwMDcwNDAtMTg2MzEzOTVmYjUxMDBiIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218631395fb4e22-0f64390783d3e48-16525635-2007040-18631395fb5100b%22%7D; _ga=GA1.1.1291950143.1675863090; _ga_9PQ283MLZQ=GS1.1.1675869151.2.1.1675870581.0.0.0',
        'Pragma': 'no-cache',
        'Referer': 'https://indices.cnfin.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }
    now_time = str(int(time.time() *1000))
    jsonpcallback = 'jQuery19108766575911147751_{0}'.format(now_time)
    params = {
        'jsonpcallback': jsonpcallback,
        'ids': str(id),
        'type': '1',
        '_': now_time,
    }
    print(now_time)
    response = requests.get('https://api.cnfin.com/roll/charts/getContent', params=params, cookies=cookies, headers=headers)
    ret_text = response.text.replace(jsonpcallback, '')[1:-1]
    print(ret_text)
    json_ret = json.loads(ret_text)['data']['list'][0]
    # print(json_ret)
    content = json.loads(json_ret['content'])
    for con in content:
        print(con)
        all_info.append([
            con['x'],con['y']
        ])

if __name__ == '__main__':
    all_info = [['日期', '值']]
    id = 14856
    main(id)
    df = pd.DataFrame(all_info)
    df.to_excel('data-{0}.xlsx'.format(id))
