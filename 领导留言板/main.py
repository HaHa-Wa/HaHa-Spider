# # -*- coding: utf-8 -*-
# """
# @Time ： 2023/2/1 10:32 下午
# @Auth ： HaHa-Wa
# @File ：main.py
# @IDE ：PyCharm
# """
import hashlib
import json
import time

import requests
import pandas as pd


# from  utils.common import common
def time_date(timestamp):
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(精确到秒)
    dt = time.strftime("%Y-%m-%d %H:%M", time_local)
    return dt


def get_detail(ID):
    param = {"tid": str(ID), "fromTrash": 0}
    s_s = '/v1/threads/content' + json.dumps(param).replace(' ', '') + "a2eb17f65d6f4b3f"

    res = hashlib.md5(s_s.encode(encoding='UTF-8')).hexdigest()
    json_data = {
        'appCode': 'PC42ce3bfa4980a9',
        'token': '',
        'signature': res,
        'param': json.dumps(param).replace(' ', ''),
    }

    response = requests.post(
        'http://liuyan.people.com.cn/v1/threads/content',
        headers=headers,
        json=json_data,
        verify=False,
    )
    json_ret = json.loads(response.text)['resultData']['contentList']
    print(json_ret)
    try:
        reply_1 = json_ret[1]['content']
        reply_1_time = json_ret[1]['dateline']
        organization = json_ret[1]['organization']
    except:
        reply_1 = ''
        reply_1_time = ''
        organization = ''
    try:
        content = json_ret[2]['content']
        nickName = json_ret[2]['nickName']
        stateInfo = json_ret[2]['stateInfo']
        tags = json_ret[2]['tags']
    except:
        content = ''
        nickName = ''
        stateInfo = ''
        tags = ''
    print(reply_1, reply_1_time, organization, content, nickName, stateInfo)
    return reply_1, reply_1_time, organization, content, nickName, stateInfo


def main():

    url = 'http://liuyan.people.com.cn/v1/threads/list/df'
    for typeId in [5,2,1]:
        lastItem = ''

        while True:
            param = {
                "fid": 585,
                "showUnAnswer": 1,
                "typeId": typeId,
                "lastItem": lastItem,
                "position": "0",
                "rows": 10,
                "orderType": 2
                }
            s_s = '/v1/threads/list/df' + json.dumps(param).replace(' ', '') + "a2eb17f65d6f4b3f"

            res = hashlib.md5(s_s.encode(encoding='UTF-8')).hexdigest()

            data = {
                "appCode": 'PC42ce3bfa4980a9',
                "param": json.dumps(param).replace(' ', ''),
                "signature": res,
                "token": ""
            }
            # print(data)
            ret = requests.post(url, headers=headers, json=data)
            json_ret = json.loads(ret.content.decode())
            resultData = json_ret['resultData']['data']
            for x in resultData:
                print(x)
                ID = x['tid']
                reply_1, reply_1_time, organization, content, nickName, stateInfo = get_detail(ID)
                x['reply_12'] = reply_1
                x['reply_1_time2'] = reply_1_time
                x['organization2'] = organization
                x['content2'] = content
                x['nickName2'] = nickName
                x['stateInfo2'] = stateInfo
                x['createDateline'] = time_date(x['createDateline'])
                x['dateline'] = time_date(x['dateline'])
                x['threadsCheckTime'] = time_date(x['threadsCheckTime'])

                try:
                    x['lastAnswerTime'] = time_date(x['lastAnswerTime'])
                except:
                    pass
                # x['createDateline'] = time_date(x['createDateline'])

                all_info.append(x)
            lastItem = resultData[-1]['tid']
            if len(resultData) < 10:
                break
            # break
        # break


if __name__ == '__main__':
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Cookie': '4de1d0bdb25d4625be2481a1b9e1350f=WyIyMDQ3MDc5Nzk3Il0; __jsluid_h=c06e1ec02bc274b0456538b3f700c902; language=zh-CN',
        'Origin': 'http://liuyan.people.com.cn',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://liuyan.people.com.cn/threads/list?checkStatus=0&fid=585&formName=%E8%B4%B5%E5%B7%9E%E7%9C%81%E5%A7%94%E4%B9%A6%E8%AE%B0%E5%BE%90%E9%BA%9F&position=0&province=35&saveLocation=27&pForumNames=%E8%B4%B5%E5%B7%9E%E7%9C%81',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'token': '',
    }
    all_info = []
    # get_detail()
    main()
    df = pd.DataFrame(all_info)
    df.to_excel('留言数据-省委书记.xlsx')
