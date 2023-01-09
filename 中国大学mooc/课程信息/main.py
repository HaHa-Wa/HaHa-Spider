import datetime
import time

import requests
from bs4 import BeautifulSoup
import pandas as pd
from retrying import retry


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_detail(id, shortName):
    url = f'https://www.icourse163.org/course/{shortName}-{id}'
    print(url)
    ret = requests.get(url, headers=headers)
    res = BeautifulSoup(ret.text, 'lxml')
    div = res.find('div', id='content-section')
    try:
        miaoshu = div.find('div', class_='f-richEditorText').text
    except:
        miaoshu = '-'
    try:
        mubiao = div.find_all('div', class_='f-richEditorText')[1].text
    except:
        mubiao = '-'
    try:
        dagang = div.find('div', {'class': 'outline'}).text.replace('\xa0', '')
    except:
        dagang = ''
    try:
        yaoqiu = div.find('div', class_='category-content j-cover-overflow certRope').text
    except:
        yaoqiu = ''
    try:
        ziliao = div.find_all('div', {'class': 'category-content j-cover-overflow'})[3].text
    except:
        ziliao = ''
    # print('miaoshu', miaoshu)
    return miaoshu, dagang, yaoqiu, ziliao, mubiao


def time_s(time_str):
    print(time_str)
    timeArray = time.localtime(int(time_str) /1000)
    otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
    return otherStyleTime


def main():
    params = (
        ('csrfKey', '5e046a9db7c24defb130f51f5b85cbcf'),
    )
    for page in range(1, 106):
        data = {
            'mocCourseQueryVo': '{"keyword":"\u7EDF\u8BA1\u5B66","pageIndex":' + str(
                page) + ',"highlight":true,"orderBy":0,"stats":30,"pageSize":20}'
        }

        response = requests.post('https://www.icourse163.org/web/j/mocSearchBean.searchCourse.rpc', headers=headers,
                                 params=params, data=data)
        course_list = response.json()['result']['list']
        for course in course_list:
            # print(course)
            mocCourseCard = course['mocCourseCard']
            try:
                mocCourseCardDto = mocCourseCard['mocCourseCardDto']
            except:
                continue
            enrollCount = mocCourseCard['enrollCount']
            startTime = time_s(mocCourseCardDto['termPanel']['startTime'])
            endTime = time_s(mocCourseCardDto['termPanel']['endTime'])
            jsonContent = mocCourseCardDto['termPanel']['jsonContent']
            course_name = mocCourseCardDto['name']
            id = mocCourseCardDto['id']
            schoolPanel = mocCourseCardDto['schoolPanel']
            scool_name = schoolPanel['name']
            shortName = schoolPanel['shortName']
            try:
                mocTagDtos = ''.join([x['name'] for x in mocCourseCardDto['mocTagDtos']])
            except:
                mocTagDtos = ''
            lectorPanels = mocCourseCardDto['termPanel']['lectorPanels']
            try:
                teachers = '、'.join([x['realName'] for x in lectorPanels])
            except:
                teachers = ''
            print(course_name)
            # for cours in cours_list:
            # if cours in course_name:
            # if cours in miaoshu:
            miaoshu, dagang, yaoqiu, ziliao, mubiao = get_detail(id, shortName)
            cours_info.append(
                [course_name, id, enrollCount, startTime, endTime, jsonContent, scool_name, shortName, mocTagDtos, teachers, miaoshu,
                 dagang, yaoqiu, ziliao, mubiao])
        # break


if __name__ == '__main__':
    cours_list = ['抽样', '调查', '统计学', '概率论', '数理统计', '经济统计', '多元统计', '数学分析', '数据分析', '计量经济学', '时间序列分析']
    cours_info = []
    headers = {
        'authority': 'www.icourse163.org',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'NTESSTUDYSI=5e046a9db7c24defb130f51f5b85cbcf; EDUWEBDEVICE=fce2a9e03c624c12860ef37cf6aa1276; Hm_lvt_77dc9a9d49448cf5e629e5bebaa5500b=1670054911; hb_MA-A976-948FFA05E931_source=www.google.com; WM_NI=%2Be3vfkcVtNJoon%2BcTgTiLCiUu1px%2BBfyRJUdpXj%2Br24wOX5CPuZDeWiZzGL0Blf09sfHEye1wUd56yvy6QbYNaNSeV0cOaniXiamtaz48jX7kssqPjS0rF3YwMZh9a1SMWI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb4e95a85bfa786f854b4ef8eb6d15e829a9facc47089bcbba2d63d8a99fdb5bb2af0fea7c3b92ae9bbfd97e561a18abcafc965adb2e584d76d98b784a4ec5fb7efc099aa4aa6a79eabd870b488a6ccf13af8a981b9b84994ab96a5e85dab86b6a8cf3c82b4aad1bc79a6988b9ae83bb58bacd6b573b6a7fab2e1538ebf82b4e85ef4bd8182ed639cb7af8ef76bbaecf88bdb3da9adbd92d36291f0bea7b253b5939689bc6bf38d83b8cc37e2a3; WM_TID=n%2BowxSY5ULVFAARUQBKFYaY6AG%2BJWnS4; __yadk_uid=GI5k9b4w9HW3pocMFcC598xixPJS6be1; Hm_lpvt_77dc9a9d49448cf5e629e5bebaa5500b=1670055918',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    main()
    df = pd.DataFrame(cours_info)
    df.to_excel('课程3.xls')
