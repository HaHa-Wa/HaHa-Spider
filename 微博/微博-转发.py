# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/23 9:48 上午
@Auth ： HaHa-Wa
@File ：微博-转发.py
@IDE ：PyCharm
"""
import requests
import pandas as pd
from bs4 import BeautifulSoup

def main():
    cookies = {
        'SINAGLOBAL': '850174227310.1343.1653300029712',
        'UOR': ',,login.sina.com.cn',
        'SSOLoginState': '1676819392',
        'XSRF-TOKEN': 'lSopttL4bjjpJV6Jy95emV6A',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5KMhUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE',
        'ALF': '1679668731',
        'SCF': 'AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cy_KrgxSJj01-nXEzUK5E1QSnE4AI2FSbxo9rrZg-v7qA.',
        'SUB': '_2A25O8livDeRhGeFJ4loZ-CnMyDmIHXVths1nrDV8PUNbmtANLWrTkW9Nfo-3qypNDFb85sRzpvhJsbxeHlNKh-1Z',
        '_s_tentry': 'weibo.com',
        'Apache': '802052389566.9185.1677081379658',
        'ULV': '1677081379693:6:2:1:802052389566.9185.1677081379658:1675831097664',
        'WBPSESS': 'rYwReJScEM06jqB6vnCcw6i_h9Xr93E5z74CXJtmB0iYWmbhK0Evj-PqlXrjsNcZCyK_1ybO_tmWl8Nr1YrSdsI808sBd-ULKEPh7UUYoHCsVpuYXE_E30y4BBuzE80Lh2gbOTtStjeydkeq7Xgm2g==',
    }

    headers = {
        'authority': 'weibo.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'client-version': 'v2.38.11',
        # 'cookie': 'SINAGLOBAL=850174227310.1343.1653300029712; UOR=,,login.sina.com.cn; SSOLoginState=1676819392; XSRF-TOKEN=lSopttL4bjjpJV6Jy95emV6A; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5KMhUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE; ALF=1679668731; SCF=AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cy_KrgxSJj01-nXEzUK5E1QSnE4AI2FSbxo9rrZg-v7qA.; SUB=_2A25O8livDeRhGeFJ4loZ-CnMyDmIHXVths1nrDV8PUNbmtANLWrTkW9Nfo-3qypNDFb85sRzpvhJsbxeHlNKh-1Z; _s_tentry=weibo.com; Apache=802052389566.9185.1677081379658; ULV=1677081379693:6:2:1:802052389566.9185.1677081379658:1675831097664; WBPSESS=rYwReJScEM06jqB6vnCcw6i_h9Xr93E5z74CXJtmB0iYWmbhK0Evj-PqlXrjsNcZCyK_1ybO_tmWl8Nr1YrSdsI808sBd-ULKEPh7UUYoHCsVpuYXE_E30y4BBuzE80Lh2gbOTtStjeydkeq7Xgm2g==',
        'referer': 'https://weibo.com/5820068605/LlJ6nt9qs',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'server-version': 'v2023.02.17.1',
        'traceparent': '00-90db4bf37dce8793b2fa901b51a8c3eb-965368f207b60dfe-00',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'lSopttL4bjjpJV6Jy95emV6A',
    }
    page = 1
    while True:
        params = {
            'id': '4752282568361262',
            'page': str(page),
            'moduleID': 'feed',
            'count': '20',
        }

        response = requests.get('https://weibo.com/ajax/statuses/repostTimeline', params=params, cookies=cookies,
                                headers=headers)
        json_res = response.json()
        data = json_res['data']
        max_page = json_res['max_page']

        for x in data:
            text = BeautifulSoup(x['text'], 'lxml')
            a_list = text.find_all('a')
            haha = [a.text[1:] for a in a_list]
            z_username = x['user']['screen_name']
            text_raw = x['text_raw']
            verified = x['user']['verified']
            print(x['user'])
            if verified:
                verified_type_ext = x['user']['verified_type_ext']
            else:
                verified_type_ext = ''
            print(haha)
            print(x['text'])
            one_info = [z_username, text_raw, verified, verified_type_ext]
            for hh in haha:
                one_info.append(hh)
            all_info.append(one_info)
        if page == max_page:
            break
        page += 1
        # break


if __name__ == '__main__':
    all_info = []
    main()
    df = pd.DataFrame(all_info)
    df.to_excel('ret3.xlsx')

