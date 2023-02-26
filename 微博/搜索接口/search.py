# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/8 12:38 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import datetime
import re
import time

import requests
import pandas as pd
from bs4 import BeautifulSoup


def parse(response):
    """
    网页解析
    """
    html = BeautifulSoup(response.text, 'lxml')
    divs = html.find_all('div', {'action-type': 'feed_list_item'})

    # tweet_ids = re.findall(r'\d+/(.*?)\?refer_flag=1001030103_" ', html)
    for div in divs:
        try:
            p_ = div.find('p', class_='txt')
            txt = p_.text
            nickname = p_['nick-name']
            # print(txt)
            all_info.append([nickname, txt])
        except:
            pass
            # print(div)
            # break
        # print(txt)
    next_page = re.search('<a href="(.*?)" class="next">下一页</a>', response.text)
    if next_page:
        url = "https://s.weibo.com" + next_page.group(1)
        ret = requests.get(url, headers=headers)
        parse(ret)
        # time.sleep(0.5)

def get_info(url):
    ret = requests.get(url, headers=headers)
    parse(ret)


def start_requests():
    """
    爬虫入口
    """

    data_list = [['2019-06-20', '2019-06-30'], ['2020-10-20', '2020-10-30'], ['2022-03-20', '2022-03-30']]
    # 这里keywords可替换成实际待采集的数据
    for data_ in data_list:
        start_time = datetime.datetime.strptime(data_[0], '%Y-%m-%d')
        end_time = datetime.datetime.strptime(data_[1], '%Y-%m-%d')
        time_spread = datetime.timedelta(days=1)
        keyword = ['华中科技大学', '华科大', '华中大']
        for word in keyword:
            urls = []
            while start_time <= end_time:
                day_string = start_time.strftime("%Y-%m-%d")
                # for hour in range(1, 24):
                start_string = day_string + '-0'
                end_string = day_string + '-23'
                url = f"https://s.weibo.com/weibo?q={word}&timescope=custom%3A{start_string}%3A{end_string}&page=1"
                print(url)
                urls.append(url)
                start_time = start_time + time_spread
            for url in urls:
                ret = requests.get(url, headers=headers)
                parse(ret)
                # break
                time.sleep(0.5)


if __name__ == '__main__':
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "cookie": "SINAGLOBAL=850174227310.1343.1653300029712; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFZjb1l2JINPs2q749ry5n-5JpX5KMhUgL.FoMN1KnR1hM7e0-2dJLoI0QLxKnL1heL1KqLxKBLB.2L1hqLxK-LBo5LBo2LxK-LBKBL1-2LxK-L1K5L1heLxKML1hzLBo.EehzE; wvr=6; ALF=1678423067; SSOLoginState=1675831070; SCF=AqLmbOdh0RLq_K-KohI8j7RAONzGuttiLOmEHCU3J3cymyD9l7TmVH8Ub5SdqJT_SbtJhuuQ-kZ72Ny6ZrgQ0Kw.; SUB=_2A25O51dODeRhGeFJ4loZ-CnMyDmIHXVtlc-GrDV8PUNbmtAKLWHnkW9Nfo-3qywMTAQ9eWaWzUIfxgSgDzgDb2Bb; _s_tentry=login.sina.com.cn; Apache=6360343067862.717.1675831097661; ULV=1675831097664:5:1:1:6360343067862.717.1675831097661:1673868159321; webim_unReadCount=%7B%22time%22%3A1675832286648%2C%22dm_pub_total%22%3A7%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A41%2C%22msgbox%22%3A0%7D; PC_TOKEN=00af0cbfda; WBStorage=4d96c54e|undefined"
    }
    all_info = [['nickname', 'txt']]
    start_requests()
    df = pd.DataFrame(all_info)
    df.to_excel('华中科技大.xlsx')
