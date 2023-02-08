# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/27 10:48 下午
@Auth ： HaHa-Wa
@File ：up.py
@IDE ：PyCharm
"""
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
    'authority': 'api.bilibili.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    '$cookie': '_uuid=5671971010-F94C-5D5A-A3AE-4B98C5D510AD668304infoc; buvid3=FCD1C261-D97B-0425-9A6C-53B50D054A8569147infoc; b_nut=1653893869; buvid4=DF8E0D0C-D3D7-B7C6-C634-5DCE514C8D5869147-022053014-iHpQqid4S8Q5DQQc50N24w%3D%3D; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; DedeUserID=389764192; DedeUserID__ckMd5=a63915989f104658; i-wanna-go-back=-1; b_ut=5; PVID=1; LIVE_BUVID=AUTO6616669488355704; rpdid=|(u~|||)m~R|0J\'uYYmu~|k~~; fingerprint=f3b6dc88364a08a6cc7ee972e08719cc; SESSDATA=2c8129a5%2C1684722694%2Cae549%2Ab1; bili_jct=e5eb028333fcfa66bbfc6bfb2e8d922b; buvid_fp=f3b6dc88364a08a6cc7ee972e08719cc; is-2022-channel=1; bp_video_offset_389764192=750261135320547300; innersign=0; sid=fsyugfmy; bsource=search_baidu; b_lsid=101095F61E_185F3911277',
    'origin': 'https://space.bilibili.com',
    'pragma': 'no-cache',
    'referer': 'https://space.bilibili.com/395877542/video?tid=0&page=2&keyword=&order=pubdate',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def timestamp_convert_localdate(timestamp, time_format="%Y/%m/%d %H:%M:%S"):
    # 按照当前设备时区来进行转换，比如当前北京时间UTC+8
    timeArray = time.localtime(timestamp)
    styleTime = time.strftime(str(time_format), timeArray)
    return styleTime


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
    try:
        videoData = json_aa['videoData']
    except:
        return ['', '', '', '', '', '', '']
    stat = videoData['stat']
    like = stat['like']
    coin = stat['coin']
    favorite = stat['favorite']
    share = stat['share']
    upData = json_aa['upData']
    fans = upData['fans']
    archiveCount = upData['archiveCount']
    tags = ','.join([x['tag_name'] for x in json_aa['tags']])
    return [like, coin, favorite, share, fans, archiveCount, tags]


def get_user_video(mid):
    page = 1
    while True:
        params = (
            ('mid', str(mid)),
            ('ps', '30'),
            ('tid', '0'),
            ('pn', str(page)),
            ('keyword', ''),
            ('order', 'pubdate'),
            ('order_avoided', 'true'),
            ('w_rid', 'b988762c66fd50a49d39dccd577dc57d'),
            ('wts', '1674828774'),
        )

        response = requests.get('https://api.bilibili.com/x/space/wbi/arc/search', headers=headers, params=params)
        json_ret = json.loads(response.text)
        data = json_ret['data']
        vlist = data['list']['vlist']
        page_num = data['page']['count']

        for v in vlist:
            print(v)
            aid = v['aid']
            author = v['author']
            title = v['title']
            play = v['play']
            video_review = v['video_review']
            length = v['length']
            created = timestamp_convert_localdate(int(v['created']))
            description = v['description']
            arcurl = 'https://www.bilibili.com/video/av{0}/'.format(aid)
            print(arcurl)
            [like, coin, favorite, share, fans, archiveCount, tags] = get_video_detail(arcurl)
            all_info.append([
                title, len(title), author, video_review, play, length, tags,
                like, coin, favorite, share, created, description, len(description)
            ])
            # break
            time.sleep(0.3)
        if (page * 30 - int(page_num)) >= 0:
            break
        page += 1


if __name__ == '__main__':
    # 短视频标题（字数）	短视频标题情感分析	up主	弹幕数量	观看数量	时长	关键词	点赞数量	投币数量	收藏数量	转载数量	发布时间	内容简介（字数）
    all_info = [['短视频标题', '短视频标题长度', 'up主', '弹幕数量', '观看数量',
                 '时长', '关键词', '点赞数量', '投币数量', '收藏数量', '转载数量', '发布时间', '简介', '简介字数']]


    av_id = [72270557, 517327498, 14804670, 483311105, 520819684, 1140672573, 23947287, 39737405,
             170948267, 37663924, 11646119, 1335713025, 471303350, 25876945, 304578055]
    try:
        for av in av_id:
            get_user_video(av)
    except:
        print('出错了')
    df = pd.DataFrame(all_info)
    df.to_excel('ret2.xlsx')
