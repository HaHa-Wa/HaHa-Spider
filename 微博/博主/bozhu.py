# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/20 11:55 下午
@Auth ： HaHa-Wa
@File ：bozhu.py
@IDE ：PyCharm
"""
# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/20 4:52 下午
@Auth ： HaHa-Wa
@File ：comment.py
@IDE ：PyCharm
"""
import time

import requests
import pandas as pd
from retrying import retry


# @retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_comment(uid, since_id):
    pass


def main():
    uid = '1888655105'
    params = {
        'uid': uid,
        'page': '1',
        'feature': '0',
    }

    response = requests.get('https://weibo.com/ajax/statuses/mymblog', params=params, cookies=cookies,
                            headers=headers)
    res = response.json()
    print(res)
    data = res['data']
    since_id = data['since_id']
    for x in data['list']:
        all_info.append(x)
    page = 2
    while True:
        print('page:', page)
        params = {
            'uid': uid,
            'page': str(page),
            'feature': '0',
            'since_id': since_id,
        }
        url = 'https://weibo.com/ajax/statuses/mymblog'
        response = requests.get(url, params=params, headers=headers)
        res = response.json()
        data = res['data']

        for x in data['list']:
            print(x)
            all_info.append(x)

        if data.get('since_id', 0) != 0:
            since_id = data['since_id']
            time.sleep(1)
            if len(data) < 1:
                break

        page += 1


if __name__ == '__main__':
    all_info = []
    cookies = {
        'SINAGLOBAL': '850174227310.1343.1653300029712',
        'UOR': ',,login.sina.com.cn',
        'ULV': '1675831097664:5:1:1:6360343067862.717.1675831097661:1673868159321',
        'SSOLoginState': '1676819392',
        'XSRF-TOKEN': 'lSopttL4bjjpJV6Jy95emV6A',
        'WBPSESS': 'rYwReJScEM06jqB6vnCcw6i_h9Xr93E5z74CXJtmB0iYWmbhK0Evj-PqlXrjsNcZt9VRd69Ydb9pg_o9xfX1d_goEIhV2pWyim4RNIHkMBP0seki1NmY51A8v264S84uiEbSuse_BTfiju9BtUgijA==',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5KMhUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE',
        'ALF': '1679497842',
        'SCF': 'AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cyaVKcw-KYjpkZ-z68wKnmg3HeccrxW_gbO1SUNbMwQBI.',
        'SUB': '_2A25O9_0jDeRhGeFJ4loZ-CnMyDmIHXVthWnrrDV8PUNbmtANLRbkkW9Nfo-3qzV-RL9G0pxXQrVoL8se_3BJtcLH',
    }

    headers = {
        'authority': 'weibo.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'client-version': 'v2.38.11',
        'cookie': 'SINAGLOBAL=850174227310.1343.1653300029712; UOR=,,login.sina.com.cn; ULV=1675831097664:5:1:1:6360343067862.717.1675831097661:1673868159321; SSOLoginState=1676819392; XSRF-TOKEN=lSopttL4bjjpJV6Jy95emV6A; WBPSESS=rYwReJScEM06jqB6vnCcw6i_h9Xr93E5z74CXJtmB0iYWmbhK0Evj-PqlXrjsNcZt9VRd69Ydb9pg_o9xfX1d_goEIhV2pWyim4RNIHkMBP0seki1NmY51A8v264S84uiEbSuse_BTfiju9BtUgijA==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5KMhUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE; ALF=1679497842; SCF=AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cyaVKcw-KYjpkZ-z68wKnmg3HeccrxW_gbO1SUNbMwQBI.; SUB=_2A25O9_0jDeRhGeFJ4loZ-CnMyDmIHXVthWnrrDV8PUNbmtANLRbkkW9Nfo-3qzV-RL9G0pxXQrVoL8se_3BJtcLH',
        'pragma': 'no-cache',
        'referer': 'https://weibo.com/u/1888655105',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'server-version': 'v2023.02.17.1',
        'traceparent': '00-6798d631c2ab2e0a52a759e8a68368f1-123fa918215cd4a5-00',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'lSopttL4bjjpJV6Jy95emV6A',
    }
    try:
        main()
    except:
        print('出错了。。。。')
    df = pd.DataFrame(all_info)
    df.to_excel('王潮歌.xlsx')
