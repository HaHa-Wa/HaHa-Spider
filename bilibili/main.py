# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/12 10:49 上午
@Auth ： HaHa-Wa
@File ：test.py
@IDE ：PyCharm
"""
import time

import requests
import pandas as pd
headers = {
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    '$cookie': '_uuid=5671971010-F94C-5D5A-A3AE-4B98C5D510AD668304infoc; buvid3=FCD1C261-D97B-0425-9A6C-53B50D054A8569147infoc; b_nut=1653893869; buvid4=DF8E0D0C-D3D7-B7C6-C634-5DCE514C8D5869147-022053014-iHpQqid4S8Q5DQQc50N24w%3D%3D; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; DedeUserID=389764192; DedeUserID__ckMd5=a63915989f104658; i-wanna-go-back=-1; b_ut=5; PVID=1; LIVE_BUVID=AUTO6616669488355704; rpdid=|(u~|||)m~R|0J\'uYYmu~|k~~; fingerprint=f3b6dc88364a08a6cc7ee972e08719cc; SESSDATA=2c8129a5%2C1684722694%2Cae549%2Ab1; bili_jct=e5eb028333fcfa66bbfc6bfb2e8d922b; buvid_fp=f3b6dc88364a08a6cc7ee972e08719cc; bsource=search_google; sid=5qx7l2ix; innersign=0; bp_video_offset_389764192=750124563950469200; b_lsid=A5968CC5_185A3EDA70D',
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'referer': 'https://www.bilibili.com/video/BV1Bp4y1D747/?spm_id_from=333.337.search-card.all.click&vd_source=33e66ef5dc09e101d44cc39c1b',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


def parse_two(replies_two):
    for replie in replies_two:
        member = replie['member']
        uname = member['uname']
        sex = member['sex']
        content = replie['content']
        message = content['message']
        rpid = replie['rpid']
        root_str = replie['root_str']

        all_info.append([uname, message, rpid, root_str, sex])


def parse(info):
    data = info['data']
    replies_one = data['replies']
    print(len(replies_one))
    for replie in replies_one:
        member = replie['member']
        uname = member['uname']
        sex = member['sex']
        content = replie['content']
        message = content['message']

        replies_two = replie['replies']
        rpid = replie['rpid']
        root_str = replie['root_str']
        if replies_two:
            parse_two(replies_two)
        all_info.append([uname, message, rpid, root_str, sex])


def main():
    for page in range(1, 51):
        params = (
            ('csrf', 'e5eb028333fcfa66bbfc6bfb2e8d922b'),
            ('mode', '3'),
            ('next', str(page)),
            ('oid', '735430122'),
            ('plat', '1'),
            ('type', '1'),
        )
        print('page:', page)
        url = 'https://api.bilibili.com/x/v2/reply/main'
        response = requests.get(url=url, headers=headers, params=params)
        ret = response.json()
        parse(ret)
        time.sleep(1)


if __name__ == '__main__':
    all_info = [['uname', 'message', 'rpid', 'root_str', 'sex']]
    try:
        main()
    except:
        print('出错了。。。')
    print(all_info)
    df = pd.DataFrame(all_info)
    df.to_excel('comment1.xlsx')
