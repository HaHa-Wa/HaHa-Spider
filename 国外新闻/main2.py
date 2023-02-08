# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/8 10:02 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_list():
    all_info = []
    for page in range(1, 14):
        params = {
            'keyword': 'شينجيانغ',
            'srchall': 'True',
            'typeid': '1',
            'page': str(page),
        }

        response = requests.get('https://www.almasryalyoum.com/news/index', params=params, cookies=cookies,
                                headers=headers)
        bs_ret = BeautifulSoup(response.text, 'lxml')
        news_item = bs_ret.find_all('div', class_='news')
        for item in news_item:
            # print(item)
            h2_a = item.find('a')
            title = h2_a.find('p').text
            href = 'https://www.almasryalyoum.com/' + h2_a['href']
            date_time = item.find('p', class_='town').text
            detail = get_detail(href)
            print(title)
            print(href)
            all_info.append([title, date_time, detail, href])
    df = pd.DataFrame(all_info)
    df.to_excel('almasryalyoum.xlsx')


def get_detail(href):
    response = requests.post(url=href, headers=headers)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    articleBody = bs_ret.find('div', id='NewsStory')
    print(articleBody.text)
    return articleBody.text


if __name__ == '__main__':
    cookies = {
        '___nrbi': '%7B%22firstVisit%22%3A1675820301%2C%22userId%22%3A%22942fd7fa-c108-415f-87c1-fba464aabbf2%22%2C%22userVars%22%3A%5B%5D%2C%22futurePreviousVisit%22%3A1675820301%2C%22timesVisited%22%3A1%7D',
        'compass_uid': '942fd7fa-c108-415f-87c1-fba464aabbf2',
        '__utmc': '55191419',
        '__utmz': '55191419.1675820308.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        '__SPK_UID': '49bc18c3-a751-11ed-92d8-8644b5a5f31d',
        'cf_chl_2': 'e764f0184b0069b',
        'cf_clearance': 'sULI43gmVcutCTpzDoA0qp94e61t9dkQAXiHQ_.ptfc-1675826736-0-150',
        '__utma': '55191419.2041802358.1675820302.1675820308.1675826740.2',
        '__utmt': '1',
        '__gads': 'ID=1625e54f91252664:T=1675826741:S=ALNI_Mb-L8PVzV3vU_O9-sZ4P7xrTq_CPg',
        '__gpi': 'UID=00000bb7aca6b265:T=1675826741:RT=1675826741:S=ALNI_MbIOeNRMOumeZbYZN9Qiw9p5NGPRg',
        'Location': 'Indonesia',
        '_gid': 'GA1.2.1333234489.1675826747',
        '_gat_UA-232068335-1': '1',
        '__qca': 'P0-2122867744-1675826746392',
        'udmsrc': '%7B%7D',
        '_pbjs_userid_consent_data': '3524755945110770',
        'udm_edge_floater_fcap': '%5B1675826750181%5D',
        '__utmb': '55191419.2.10.1675826740',
        '___nrbic': '%7B%22previousVisit%22%3A1675820301%2C%22currentVisitStarted%22%3A1675820301%2C%22sessionId%22%3A%227a5f06f6-71e2-4e3f-8445-844adf4db737%22%2C%22sessionVars%22%3A%5B%5D%2C%22visitedInThisSession%22%3Atrue%2C%22pagesViewed%22%3A3%2C%22landingPage%22%3A%22https%3A//www.almasryalyoum.com/%22%2C%22referrer%22%3A%22%22%7D',
        '_ga_M76HXVM1HM': 'GS1.1.1675826731.2.1.1675826753.0.0.0',
        '_ga': 'GA1.2.2041802358.1675820302',
        'FCNEC': '%5B%5B%22AKsRol96k1fz9LGlXZkzqwDRJxpVZCmuiz5iYq00FQ05ZCwDwDHm-5n7mLqZ8WQLy3zqVobGPtPjEQurtoxf2iKkaPZnBbRlLFRdvsqpvx_uaj1AFbg7CNGdcjnGJ_iABkZJ2RxD3QT3lM1JEZszuwNC0hFGKDYoEg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D',
        'udm_session': '2',
        'udm_session_rad': '1',
        'pbjs-unifiedid': '%7B%22TDID%22%3A%22a4d11d2b-3a8e-4b66-98e6-dcfbe5d3bb19%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-01-08T03%3A26%3A04%22%7D',
        'cto_bundle': 'h1_m8V84b29xSHZTQ3lTMk9PR0NNY09nYSUyRk11NlVZbWxvNnZ6OVNGMGplcm5KOE9YUFZuWHNuaVJyb0NLYk5VUXhaZHFiUXZlczV3WEpBMkZWN0QlMkJFWU9sQzVhcXNoQk1yWG83NmpqUkxVelZ4b05Vc092bjlMNXZSUXZCcHVZZUtVcDZaUGxJRG02RGV1TGFhaHpZVW1YMG5rMUdYbm1QcW1ST2N1amRMJTJGSk5idTglM0Q',
    }

    headers = {
        'authority': 'www.almasryalyoum.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': '__qca=P0-2122867744-1675826746392; ___nrbi=%7B%22firstVisit%22%3A1675820301%2C%22userId%22%3A%22942fd7fa-c108-415f-87c1-fba464aabbf2%22%2C%22userVars%22%3A%5B%5D%2C%22futurePreviousVisit%22%3A1675820301%2C%22timesVisited%22%3A1%7D; compass_uid=942fd7fa-c108-415f-87c1-fba464aabbf2; __utmc=55191419; __utmz=55191419.1675820308.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __SPK_UID=49bc18c3-a751-11ed-92d8-8644b5a5f31d; __utma=55191419.2041802358.1675820302.1675820308.1675826740.2; __gads=ID=1625e54f91252664:T=1675826741:S=ALNI_Mb-L8PVzV3vU_O9-sZ4P7xrTq_CPg; __gpi=UID=00000bb7aca6b265:T=1675826741:RT=1675826741:S=ALNI_MbIOeNRMOumeZbYZN9Qiw9p5NGPRg; Location=Indonesia; _gid=GA1.2.1333234489.1675826747; __qca=P0-2122867744-1675826746392; udmsrc=%7B%7D; _pbjs_userid_consent_data=3524755945110770; udm_session_rad=1; pbjs-unifiedid=%7B%22TDID%22%3A%22a4d11d2b-3a8e-4b66-98e6-dcfbe5d3bb19%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222023-01-08T03%3A26%3A04%22%7D; ASP.NET_SessionId=xn20iughe1kql5mkjdae5j12; __RequestVerificationToken=3FwCKFsvrkzqAYlo1KpEk-YGDkx-4rK_-7X_unroXDITqYM447iTHcqpNzSw5KaCxWStuc9p1KpqW_kmPdPnQDTNuLQ1JG7qXc9NBT08jls1; _pubcid=907aa1a7-2afc-4849-a742-0d4c052a39d4; _lr_retry_request=true; _lr_env_src_ats=false; panoramaId_expiry=1676431959797; _cc_id=efc8f84ef541c74d4f967e7b41aadf1b; panoramaId=b523a001ee8b11b97c870b5f6e2b16d53938c955b0c986d7f7fa0ad78b6e315b; __utmt=1; _parrable_id=tpc%253A0%252CtpcUntil%253A1675914142%252CfilteredUntil%253A1675914142%252CfilterHits%253A0; cto_bidid=iMSRxl84b29xSHZTQ3lTMk9PR0NNY09nYSUyRk9sVjh3Y1ExdWlPbUFodUNoZmdqZmVtSEhjV3QxU2JreDd2MmNjSXZaRm1GbURLcGRac3ppWHduSXhRM2FTcWhiVlp4dmc1NGlWVlM0aWNRQjYyTjBuSWNmOFdwSG9Cb096UmRjTWRBM0VaM0NYJTJGRmtoSUFlMFB6RlNsZlNhMTlCYjlmJTJCZHprRTdzZTIyRzhPa3l3MzglM0Q; cf_chl_2=18cb4041755d371; cf_clearance=IMtaa_KddtelJDbBPinUr4LC6c8hNZ55DkLRLdRTC3Q-1675828027-0-150; _ga_M76HXVM1HM=GS1.1.1675826731.2.1.1675828035.0.0.0; __utmb=55191419.23.10.1675826740; ___nrbic=%7B%22previousVisit%22%3A1675820301%2C%22currentVisitStarted%22%3A1675820301%2C%22sessionId%22%3A%227a5f06f6-71e2-4e3f-8445-844adf4db737%22%2C%22sessionVars%22%3A%5B%5D%2C%22visitedInThisSession%22%3Atrue%2C%22pagesViewed%22%3A24%2C%22landingPage%22%3A%22https%3A//www.almasryalyoum.com/%22%2C%22referrer%22%3A%22%22%7D; _ga=GA1.2.2041802358.1675820302; FCNEC=%5B%5B%22AKsRol9R8D_WQp3lGjdLwrZh0LHCF5fe5E_zKA_x51V1P9gxrkTUCwXqp6hvvfMH1TQy_ppMljmhDndWYg8TgM7k2jR4XKxIdaVlShmAf-opXJIbIIBijbpc8u6V-gmoP-dDqbdWfvp6lN06nSfzpjMmDb6shRhkKg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; udm_edge_floater_fcap=%5B1675828044781%2C1675828033562%2C1675828003041%2C1675827839650%2C1675827831300%2C1675827739851%2C1675826750181%5D; udm_session=24; cto_bundle=Hin37184b29xSHZTQ3lTMk9PR0NNY09nYSUyRkU3SWJSUVM1U2lNSlZ5em1aRDBhUzF0JTJGbnY2VEk0WDRUTmRZYyUyQjY3YTdDdktCUUFnYkZzdjgzcTM2MUxoOFVlYmdFalVJcHZPYWhvUnVHTldMJTJCR2M4WW1KUXElMkJBd3pQOEN2b3pwOHRvV3hhb2d0ZU1pd2hPVWZWYkxzT3A2bTBIbUFYc0ZocFFHJTJCRzdNT1UwRG9rJTJCdyUzRA',
        'pragma': 'no-cache',
        'referer': 'https://www.almasryalyoum.com/news/index?typeID=1&keyword=%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA&selectedSectionsIDs=&from=&to=&srchAll=True',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    # get_detail()
    get_list()
