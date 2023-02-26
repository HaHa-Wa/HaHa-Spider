# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/26 2:15 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import re
import time

import pandas as pd
import dateutil.parser
import requests

url = 'https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=Mo4k90T5S&is_show_bulletin=2&is_mix=0&count=20'


def parse_time(s):
    """
    Wed Oct 19 23:44:36 +0800 2022 => 2022-10-19 23:44:36
    """
    return dateutil.parser.parse(s).strftime('%Y-%m-%d %H:%M:%S')


def parse_two_comment(comments):
    for data in comments:
        item = dict()
        item['created_at'] = parse_time(data['created_at'])
        item['_id'] = data['id']

        item['like_counts'] = 0
        item['ip_location'] = data['source']
        item['content'] = re.sub(r"\[\S+\]", "", data['text_raw'])
        item['weiboID'] = mid

        comment_user = parse_user_info(data['user'])
        one_info = list(item.values())
        one_info.extend(list(comment_user.values()))
        all_info.append(one_info)


def parse_comment(data):
    """
    解析comment
    """
    print(data)
    item = dict()
    item['created_at'] = parse_time(data['created_at'])
    item['_id'] = data['id']
    item['like_counts'] = data['like_counts']

    item['ip_location'] = data['source']
    item['content'] = re.sub(r"\[\S+\]", "", data['text_raw'])
    item['weiboID'] = mid
    comment_user = parse_user_info(data['user'])
    # item['comments'] = data['comments']
    if data['comments'] != False:
        parse_two_comment(data['comments'])
    one_info = list(item.values())
    one_info.extend(list(comment_user.values()))
    return one_info


def parse_user_info(data):
    """
    解析用户信息
    """
    # 基础信息
    user = {
        "_id": str(data['id']),
        # "avatar_hd": data['avatar_hd'],
        "nick_name": data['screen_name'],
        "verified": data['verified'],
    }
    # 额外的信息
    keys = ['description', 'followers_count', 'friends_count',
            'gender', 'location']
    for key in keys:
        if key in data:
            user[key] = data[key]
    if 'created_at' in data:
        user['created_at'] = parse_time(data.get('created_at'))
    return user


def parse(response, mid):
    """
    网页解析
    """
    data = json.loads(response.text)['data']
    print(data)
    for comment_info in data['data']:
        try:
            item = parse_comment(comment_info)
        except:
            continue
        # print(item)
        all_info.append(item)
    if data.get('max_id', 0) != 0:
        # url = source_url + '&max_id=' + str(data['max_id'])
        url = f'https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id={data["max_id"]}&max_id_type=0'
        print(url)
        time.sleep(2)
        parse(ss_req.get(url, headers=headers), mid)


if __name__ == '__main__':
    headers = {
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'X-XSRF-TOKEN': '9d3059',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'MWeibo-Pwa': '1',
        'Referer': 'https://m.weibo.cn/p/2304135510544196_-_WEIBO_SECOND_PROFILE_WEIBO',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-platform': '"macOS"',
        'cookie': '__bid_n=1858a57cc27fa3cca24207; FPTOKEN=YGdMjFLFI56Lwy5gaYZx19wVoOYNFqjJxLLOQBlmXbeZG03zcA/aNljgxGLARjR9qMYjDqUsmMC+im4h4MA472YkAlgDFLeg86hmRjEcOpCVRulSQyHuhicJXn9gFG9eObTg+5HyeLo5FOJ89+cIrlwYpaOH+C/ubQyDfB3s/gxBW1ZTFwbsAO2CAcwZx/0qXFT3PgkdEMt5EhN7SBGE9obgoa4ZELLhow6OYLPSzrGgoT0LFGW9ocTsCLAqkpysOZl7tWAYwoHOt5GSh5xSbwN/+J4T6lMFuTS61soUVNZ6lOPWM0/491vqQrsuofwgfVqCSgcPIwIP3k/LsfJAdyqZtBAwU1Q95/InbJg5Xl50DF8pbDaLCuNdcBaQe/vjidugLwMlQ+5HyQs/xxEjNw==|pCf3WomVCy++ZW62RkZAA+VOtvzGrxPkj0jwboqdDtY=|10|05afb783b883628aa51e5dfc62f912e8; _T_WM=13198792794; WEIBOCN_FROM=1110003030; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5K-hUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE; SCF=AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cyiwaUb_ffAyfNNgaAPdGXrKd3S0ns4LdbXr9HmS7Atl4.; SUB=_2A25O93R1DeRhGeFJ4loZ-CnMyDmIHXVqGBw9rDV6PUJbktANLWj1kW1Nfo-3qyBKKpoakwy8Am2zjeW-WH5jjeoo; SSOLoginState=1676870693; ALF=1679462693; MLOGIN=1; XSRF-TOKEN=089553; M_WEIBOCN_PARAMS=oid%3D4850622781989939%26luicode%3D20000061%26lfid%3D4850622781989939%26uicode%3D20000061%26fid%3D4850622781989939'
    }
    all_info = [['评论时间', '评论ID', '点赞', 'IP属地', '内容', '微博ID', '用户ID', '用户名', '是否认证',
                 '签名', '粉丝数', '关注数', '性别', '位置']]

    # 这里tweet_ids可替换成实际待采集的数据
    # '',
    tweet_ids = [
        '4850622781989939']
    # try:
    ss_req = requests.session()
    for mid in tweet_ids:
        url = f'https://m.weibo.cn/comments/hotflow?id={mid}&mid={mid}&max_id_type=0'
        ret = ss_req.get(url, headers=headers)
        parse(ret, mid)
    # except:
    #     print('出错了。。。。', mid)
    df = pd.DataFrame(all_info)
    df.to_excel('test2.xlsx')
