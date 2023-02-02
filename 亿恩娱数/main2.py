# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/14 11:53 下午
@Auth ： HaHa-Wa
@File ：main2.py
@IDE ：PyCharm
"""
# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/14 9:12 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import json
import time
import requests
import pandas as pd


def get_info(MovieID, EntMovieID):
    data = {
        'r': '0.7167395130784935',
        'entmovieid': EntMovieID,
        'movieid': MovieID
    }

    response = requests.post('https://ys.endata.cn/enlib-api/api/movie/getmovie_baseinfo.do', headers=headers,
                             cookies=cookies, data=data)
    ret = response.json()
    data = ret['data']
    table0 = data['table0'][0]
    Actor = table0['Actor']  # 演员
    Country = table0['Country']  # 国家地区
    Genre = table0['Genre']  # 类型
    GenreMain = table0['GenreMain']  # 主类型
    MovieName = table0['MovieName']  # 电影名
    ReleaseDate = table0['ReleaseDate']  # 发布日期
    MovieFormat = table0['MovieFormat']  # 制式
    Director = table0['Director']  # 导演
    RunTime = table0['RunTime']
    table4 = data['table4']
    print(table4)
    chupin = ''
    zhizuo = ''
    faxing = ''
    for ha in table4:
        if ha['CompanyTypeName'] == '出品公司':
            chupin = ha['CompanyNames']
        if ha['CompanyTypeName'] == '发行公司':
            faxing = ha['CompanyNames']
        if ha['CompanyTypeName'] == '制作公司':
            zhizuo = ha['CompanyNames']

    one_info = [MovieName, Actor, Country, Genre, GenreMain, ReleaseDate,
                MovieFormat, Director, RunTime, chupin, zhizuo, faxing]
    print(one_info)
    return one_info


def get_list():
    for page in range(1, 6):
        data = {
            'r': '0.3761928300037318',
            'datetype': 'Year',
            'date': '2018-01-01,2022-12-31',
            'sdate': '2018-01-01',
            'edate': '2022-12-31',
            'dateid': '2018,2022',
            'sdateid': '2018',
            'edateid': '2022',
            'bserviceprice': '1',
            'columnslist': '100,201,101,102,107,115,103,116,104,117,118,105,106',
            'pageindex': str(page),
            'pagesize': '20',
            'order': '102',
            'ordertype': 'desc'
        }
        url = 'https://ys.endata.cn/enlib-api/api/movie/getMovie_BoxOffice_Year_List.do'
        response = requests.post(url, headers=headers,
                                 cookies=cookies, data=data)
        data = response.json()['data']['table1']
        print(len(data))
        for x in data:
            print(x)
            all_info.append(x)


def get_piaofang(EntMovieID):
    data = {
        'r': '0.7004936670901978',
        'entmovieid': EntMovieID
    }

    response = requests.post('https://ys.endata.cn/enlib-api/api/movie/getMovie_HeadBoxOfficeByMovieID.do',
                             headers=headers, cookies=cookies, data=data)
    res = response.json()['data']['table0'][0]
    BoxOfficeToTal = res['BoxOfficeToTal']
    ShowCountALL = res['ShowCountALL']
    AudienceCountALL = res['AudienceCountALL']
    BoxOfficeFirstDay = res['BoxOfficeFirstDay']
    BoxOfficeFirstWeek = res['BoxOfficeFirstWeek']
    BoxOfficeWeekEnd = res['BoxOfficeWeekEnd']
    MaoYanWantToSee = res['MaoYanWantToSee']
    MaoYanScore = res['MaoYanScore']
    TaoPiaoPiaoWantToSee = res['TaoPiaoPiaoWantToSee']
    TaoPiaoPiaoScore = res['TaoPiaoPiaoScore']
    DouBanWantToSee = res['DouBanWantToSee']
    DouBanScore = res['DouBanScore']
    return [BoxOfficeToTal, ShowCountALL, AudienceCountALL, BoxOfficeFirstDay, BoxOfficeFirstWeek,
            BoxOfficeWeekEnd, MaoYanWantToSee, MaoYanScore, TaoPiaoPiaoWantToSee, TaoPiaoPiaoScore, DouBanWantToSee,
            DouBanScore]


def main():
    with open('list2.json', 'r', encoding='utf-8')as f:
        info_list = f.read()
    for obj in json.loads(info_list):
        MovieID = obj['MovieID']
        EntMovieID = obj['EntMovieID']
        BoxOffice = obj['BoxOffice']
        TotalBoxOffice = obj['TotalBoxOffice']
        print(obj)
        one_info = get_info(MovieID, EntMovieID)
        one_info_2 = get_piaofang(EntMovieID)
        one_info.extend(one_info_2)
        all_info.append(one_info)
        time.sleep(0.3)
        # break


if __name__ == '__main__':
    cookies = {
        'JSESSIONID': 'e0368dee-d755-4a05-8967-8c28be239652',
        'route': '65389440feb63b53ee0576493abca26d',
        'Hm_lvt_82932fc4fc199c08b9a83c4c9d02af11': '1673681548,1673701671',
        'Hm_lpvt_82932fc4fc199c08b9a83c4c9d02af11': '1673711652',
    }
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://ys.endata.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://ys.endata.cn/Details/Movie?entId=682630',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    all_info = [['影片名称', '演员', '国别', '类型', '主类型',
                 '上映日期', '影片制式', '导演', '时长', '出品公司', '制作公司',
                 '发行公司', '累计票房', '累计场次', '累计人次', '首映日票房', '首周票房', '首周末票房',
                 '猫眼人次', '猫眼评分', '淘票票人次', '淘票票人次', '豆瓣人次', '豆瓣人次']]
    # get_piaofang()
    try:
        main()
    except:
        print('出错了')
    df = pd.DataFrame(all_info)
    df.to_excel('ret2.xlsx')
    # all_info = []
    # get_list()
    # with open('list2.json', 'w', encoding='utf-8')as f:
    #     # info_list = f.read()
    #     json.dump(all_info, f, ensure_ascii=False)
