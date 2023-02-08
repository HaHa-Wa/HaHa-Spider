# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/29 8:20 下午
@Auth ： HaHa-Wa
@File ：danmu.py
@IDE ：PyCharm
"""
import re
import requests
import pandas as pd
import time
from tqdm import trange

# 视频页面点击“浏览器地址栏小锁-Cookie-bilibili.com-Cookie-SESSDATA”进行获取
SESSDATA = "2c8129a5%2C1684722694%2Cae549%2Ab1"
# 视频页面“按F12-Console-输入document.cookie”进行获取
cookie = "_uuid=5671971010-F94C-5D5A-A3AE-4B98C5D510AD668304infoc; buvid3=FCD1C261-D97B-0425-9A6C-53B50D054A8569147infoc; b_nut=1653893869; buvid4=DF8E0D0C-D3D7-B7C6-C634-5DCE514C8D5869147-022053014-iHpQqid4S8Q5DQQc50N24w%3D%3D; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; CURRENT_FNVAL=4048; DedeUserID=389764192; DedeUserID__ckMd5=a63915989f104658; i-wanna-go-back=-1; b_ut=5; PVID=1; LIVE_BUVID=AUTO6616669488355704; rpdid=|(u~|||)m~R|0J'uYYmu~|k~~; SESSDATA=2c8129a5%2C1684722694%2Cae549%2Ab1; bili_jct=e5eb028333fcfa66bbfc6bfb2e8d922b; is-2022-channel=1; sid=6xfi4dn0; bp_video_offset_389764192=755843291466956900; b_lsid=57C5557D_185FD286D06; innersign=1; share_source_origin=COPY; fingerprint=39796ad94faa0d66a58919ef691f7c26; buvid_fp=b0fda9066980a9e583468dfa1a7f0520; bsource=share_source_copy_link"
cookie += f";SESSDATA={SESSDATA}"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "cookie": cookie,
}


def get_info(vid):
    url = f"https://api.bilibili.com/x/web-interface/view/detail?bvid={vid}"
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    data = response.json()
    info = {}
    info["标题"] = data["data"]["View"]["title"]
    info["总弹幕数"] = data["data"]["View"]["stat"]["danmaku"]
    info["视频数量"] = data["data"]["View"]["videos"]
    info["cid"] = [dic["cid"] for dic in data["data"]["View"]["pages"]]
    if info["视频数量"] > 1:
        info["子标题"] = [dic["part"] for dic in data["data"]["View"]["pages"]]
    for k, v in info.items():
        print(k + ":", v)
    return info


def get_danmu(info, start, end):
    date_list = [i for i in pd.date_range(start, end).strftime("%Y-%m-%d")]
    all_dms = []
    for i, cid in enumerate(info["cid"]):
        dms = []
        for j in trange(len(date_list)):
            url = f"https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid={cid}&date={date_list[j]}"
            response = requests.get(url, headers=headers)
            response.encoding = "utf-8"
            data = re.findall(r"[:](.*?)[@]", response.text)
            dms += [dm[1:] for dm in data]
            time.sleep(3)
        if info["视频数量"] > 1:
            print("cid:", cid, "弹幕数:", len(dms), "子标题:", info["子标题"][i])
        all_dms += dms
    print(f"共获取弹幕{len(all_dms)}条！")
    return all_dms


if __name__ == "__main__":
    # vid = input("输入视频编号: ")
    vid = 'BV1zD4y1H7fo'
    info = get_info(vid)
    start = input("输入弹幕开始时间（年-月-日）: ")
    end = input("输入弹幕结束时间（年-月-日）: ")
    danmu = get_danmu(info, start, end)
    with open("danmu.txt", "w", encoding="utf-8") as fout:
        for dm in danmu:
            fout.write(dm + "\n")
