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


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_comment(mid, max_id):
    params = {
        'flow': '0',
        'is_reload': '1',
        'id': mid,
        'is_show_bulletin': '2',
        'is_mix': '0',
        'max_id': max_id,
        'count': '50',
        'uid': '5145725878',
    }
    url = 'https://weibo.com/ajax/statuses/buildComments'
    response = requests.get(url, params=params, cookies=cookies,
                            headers=headers, verify=False, timeout=3)
    res = response.json()
    data = res['data']
    for x in data:
        print(x['text'])
        x['original'] = mid
        all_info.append(x)

    if res.get('max_id', 0) != 0:
        max_id = res['max_id']
        time.sleep(1)
        if len(data) > 1:
            get_comment(mid, max_id)


def main():
    mid_list = [4850622781989939,
                4842331268717934,
                4849249411925259,
                4842279603276339,
                4841908414972604,
                4857506810301622,
                4848083597263855,
                4857871618019232,
                4843764151226448,
                4842724689975584,
                4851346513860853,
                4846712454395619,
                4848434543331050,
                4844115684757915,
                4843750012231909,
                4843798556846211,
                4850335425770942,
                4843738088086783,
                4843431081548419,
                4842334069466716,
                4855771245056485,
                4848446969743081,
                4857870459603736,
                4843762981277097,
                4843012419229345,
                4843738704380488,
                4851709916479588,
                4843074398722298,
                4842677110049791,
                4844901022307673,
                4857944632465070,
                4841938962093671,
                4857866462435478,
                4857865707198105,
                4858945322093847,
                4843028747651214,
                4845913095277255,
                4844174597950221,
                4850985862957211,
                4841941705432943,
                4842657845354158,
                4843723320197227,
                4844536880700560,
                4842634873409185,
                4856493997820181,
                4842303329927779,
                4851709777811473,
                4859374906902033,
                4842643663623770,
                4841967793475063]
    for mid in mid_list:
        params = {
            'is_reload': '1',
            'id': mid,
            'is_show_bulletin': '2',
            'is_mix': '0',
            'count': '50',
            'uid': '5145725878',
        }

        response = requests.get('https://weibo.com/ajax/statuses/buildComments', params=params, cookies=cookies,
                                headers=headers)
        res = response.json()
        max_id = res['max_id']
        data = res['data']
        for x in data:
            x['original——mid'] = mid
            all_info.append(x)
        get_comment(mid, max_id)


if __name__ == '__main__':
    all_info = []
    cookies = {
        'SINAGLOBAL': '850174227310.1343.1653300029712',
        'UOR': ',,login.sina.com.cn',
        'ULV': '1675831097664:5:1:1:6360343067862.717.1675831097661:1673868159321',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5KMhUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE',
        'ALF': '1679411391',
        'SSOLoginState': '1676819392',
        'SCF': 'AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cy7ChRvPXIrrbTdnf41ee3zcnzfQuuUB2BjC_Aag6jGjk.',
        'SUB': '_2A25O9kuQDeRhGeFJ4loZ-CnMyDmIHXVtgjpYrDV8PUNbmtANLWnFkW9Nfo-3qznNTHASgWNM7yV4x4sCixWsJARw',
        'XSRF-TOKEN': 'lSopttL4bjjpJV6Jy95emV6A',
        'WBPSESS': 'rYwReJScEM06jqB6vnCcw6i_h9Xr93E5z74CXJtmB0iYWmbhK0Evj-PqlXrjsNcZCyK_1ybO_tmWl8Nr1YrSdnNHzy-V4eQ3IPmTAW0-183gWN5QIIRGKppWwU4KJX2UAz7iILw2kEtEeBnGYaYO6Q==',
    }

    headers = {
        'authority': 'weibo.com',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        # 'x-xsrf-token': 'lSopttL4bjjpJV6Jy95emV6A',
    }
    # try:
    main()
    # except:
    #     print('出错了。。。。')
    df = pd.DataFrame(all_info)
    df.to_excel('comment.xlsx')
