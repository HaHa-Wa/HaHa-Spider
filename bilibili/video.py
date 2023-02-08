# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/12 7:55 下午
@Auth ： HaHa-Wa
@File ：video.py
@IDE ：PyCharm
"""
import json
import re
import time

import pandas as pd

import requests

headers = {
    'authority': 's.search.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    '$cookie': '_uuid=5671971010-F94C-5D5A-A3AE-4B98C5D510AD668304infoc; buvid3=FCD1C261-D97B-0425-9A6C-53B50D054A8569147infoc; b_nut=1653893869; buvid4=DF8E0D0C-D3D7-B7C6-C634-5DCE514C8D5869147-022053014-iHpQqid4S8Q5DQQc50N24w%3D%3D; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; DedeUserID=389764192; DedeUserID__ckMd5=a63915989f104658; i-wanna-go-back=-1; b_ut=5; PVID=1; LIVE_BUVID=AUTO6616669488355704; rpdid=|(u~|||)m~R|0J\'uYYmu~|k~~; fingerprint=f3b6dc88364a08a6cc7ee972e08719cc; SESSDATA=2c8129a5%2C1684722694%2Cae549%2Ab1; bili_jct=e5eb028333fcfa66bbfc6bfb2e8d922b; buvid_fp=f3b6dc88364a08a6cc7ee972e08719cc; bsource=search_google; sid=5qx7l2ix; bp_video_offset_389764192=750124563950469200; innersign=0; b_lsid=F21EE2A8_185A5C39C56; is-2022-channel=1',
    'origin': 'https://www.bilibili.com',
    'pragma': 'no-cache',
    'referer': 'https://www.bilibili.com/v/knowledge/business',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}


def get_user_info(mid):
    url = 'https://api.bilibili.com/x/space/navnum?mid=1264115421' % mid
    ret = requests.get(url, headers=headers)
    res = json.loads(ret.content.decode())['data']['video']
    return res


def get_video_detail(url):
    # url = 'https://www.bilibili.com/video/av850549772/'
    haha = requests.get(url, headers=headers)
    res = haha.content.decode()
    # print(res)
    aa = re.findall('window.__INITIAL_STATE__=(.*?);\(function', res)[0]
    # print(aa)
    json_aa = json.loads(aa)
    videoData = json_aa['videoData']

    stat = videoData['stat']
    like = stat['like']
    coin = stat['coin']
    favorite = stat['favorite']
    share = stat['share']
    upData = json_aa['upData']
    fans = upData['fans']
    archiveCount = upData['archiveCount']
    return [like, coin, favorite, share, fans, archiveCount]


def get_video():
    for page in range(76, 87):
        print('page:', page)
        params = (
            ('main_ver', 'v3'),
            ('search_type', 'video'),
            ('view_type', 'hot_rank'),
            ('copy_right', '-1'),
            ('new_web_tag', '1'),
            ('order', 'click'),
            ('cate_id', '207'),
            ('page', str(page)),
            ('pagesize', '30'),
            ('time_from', '20220101'),
            ('time_to', '20220131'),
        )

        response = requests.get('https://s.search.bilibili.com/cate/search', headers=headers, params=params)
        json_ret = json.loads(response.content.decode())
        result = json_ret['result']
        for x in result:
            arcurl = x['arcurl']
            vname = x['title']
            print(vname)
            shichang = x['duration']
            mid = x['mid']
            tag = x['tag']
            rank_score = x['rank_score']  # 播放量
            favorites = x['favorites']  # 收藏量
            senddate = x['senddate']  # 发布时间
            video_review = x['video_review']  # 弹幕
            [like, coin, favorite, share, fans, archiveCount] = get_video_detail(arcurl)
            all_info.append(
                [vname, rank_score, fans, archiveCount, shichang, tag, like, coin, favorites, share, video_review])
            # break
            time.sleep(0.3)


if __name__ == '__main__':
    all_info = [['视频名称', '播放量', 'up主粉丝数', 'up主投稿数', '视频时长',
                 '视频下方所有tag', '点赞数', '投币数', '收藏量', '转发量', '弹幕数']]
    try:
        get_video()
    except:
        print('出错了')
    df = pd.DataFrame(all_info)
    df.to_excel('ret4.xlsx')
