# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/1 3:12 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import numpy
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pymongo import MongoClient
from retrying import retry


def get_zhuliao(ret):
    z_dict = {}
    strongs = ret.find_all('strong')
    for st in strongs:
        a = st.find('a').text
        v = st.text.replace(a, '')
        z_dict[a] = v
    return z_dict


def parse_box(recipe_step_box):
    haha = []
    step_contents = recipe_step_box.find_all('div', class_='step_content')
    for step in step_contents:
        try:
            a1 = step.find('img')['src']
        except:
            a1 = numpy.nan
        try:
            a2 = step.find('p').text
        except:
            a2 = numpy.nan
        haha.append((a1, a2))
    return haha


def parse_detail(bs_ret, url):
    recipe_step_box = bs_ret.find('div', class_='recipe_step_box')
    title = bs_ret.find('h1', class_='recipe_title').text
    gongyi = bs_ret.find('div', class_='info2_item info2_item1').find('strong').text
    kouwei = bs_ret.find('div', class_='info2_item info2_item2').find('strong').text
    shijian = bs_ret.find('div', class_='info2_item info2_item3').find('strong').text
    nandu = bs_ret.find('div', class_='info2_item info2_item4').find('strong').text
    try:
        recipe_topimg = bs_ret.find('img', class_='recipe_topimg')['src']
        recipe_topvideo = numpy.nan
    except:
        recipe_topimg = bs_ret.find('img', class_='recipe_topvideo_bg')['src']
        recipe_topvideo = bs_ret.find('video', id='main_video')['src']
    zhuliao = bs_ret.find('div', class_='recipe_ingredients').find('div', class_='right')
    zhuliao = get_zhuliao(zhuliao)
    fuliao = bs_ret.find('div', class_='recipe_ingredients recipe_ingredients1').find('div', class_='right')
    fuliao = get_zhuliao(fuliao)
    try:
        tang = bs_ret.find('div', class_='dataitem').find('div', class_='c1').text + '克'
    except:
        tang = numpy.nan
    try:
        reliang = bs_ret.find_all('div', class_='dataitem')[1].find('div', class_='c1').text + '大卡'
    except:
        reliang = numpy.nan
    try:
        zhifang = bs_ret.find_all('div', class_='dataitem')[2].find('div', class_='c1').text + '克'
    except:
        zhifang = numpy.nan

    fitme_items = bs_ret.find('div', class_='fitme_items')
    # if fitme_items:
    try:
        fanliang = bs_ret.find('span', class_='rf').text.replace('人份', '')
    except:
        fanliang = numpy.nan
    try:
        fitme_items = fitme_items.find_all('div', class_='fitme_item')
        fitme_dict = {}
        for fitm in fitme_items:
            hh = fitm.find('div', class_='t').text
            jj = fitm.find('p').text
            fitme_dict[hh] = jj
        jianfei = fitme_dict['减肥人群']
        gaoxieya = fitme_dict['高血压人群']
        gaoxiezhi = fitme_dict['高血脂人群']
        ertong = fitme_dict['儿童']
        gaoxietang = fitme_dict['高血糖人群']
    except:
        jianfei = numpy.nan
        gaoxieya = numpy.nan
        gaoxiezhi = numpy.nan
        ertong = numpy.nan
        gaoxietang = numpy.nan
    step_box = parse_box(recipe_step_box)
    one_list = [title, url, recipe_topimg, recipe_topvideo, gongyi, kouwei, shijian, nandu, fanliang,
                gaoxiezhi, jianfei, gaoxieya, gaoxietang, ertong,
                tang, reliang, zhifang, str(zhuliao), str(fuliao), str(recipe_step_box), str(step_box)]
    print(one_list)
    return one_list


def get_detail(href):
    # url = 'https://www.meishij.net/zuofa/jiucaijidanjiaozi_27.html'
    ret = requests.get(url=href, headers=headers)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    one_list = parse_detail(bs_ret, href)
    all_list.append(one_list)


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_s(url):
    ret = requests.get(url, headers=headers, timeout=5)
    return ret


def get_two(name1, href):
    page = 1
    if name1 == '拌面':
        page = 279
    while True:
        url = '{0}p{1}/'.format(href, page)
        print(url)
        ret = send_s(url)
        bs_ret = BeautifulSoup(ret.text, 'lxml')
        list_s2_item = bs_ret.find_all('div', class_='list_s2_item')
        for item in list_s2_item:
            href2 = item.find('a', class_='list_s2_item_img')['href']
            name2 = item.find('strong', class_='title').text
            print(name2, href2)
            # insert_mongo({
            #     'name1': name1,
            #     'name2': name2,
            #     'href': href2
            # })
            get_detail(href2)
        if len(list_s2_item) < 21:
            break
        if page == 3:
            break
        page += 1


def insert_mongo(item):
    data = dict(item)
    post.insert(data)
    return item


def get_list():
    haha = True
    url = 'https://www.meishij.net/fenlei/liangcai/'

    ret = requests.get(url, headers=headers)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    sortlist = bs_ret.find('dl', id='sortlist')
    a_list = sortlist.find_all('a')
    for x in a_list:
        href = 'https://www.meishij.net' + x['href']
        name = x.text
        print(name, href)
        if href == 'https://www.meishij.netjavascript:;':
            continue
        if name == '拌面':
            haha = True
        if haha:
            get_two(name, href)
        break


if __name__ == '__main__':
    # MONGODB_HOST = '127.0.0.1'
    # MONGODB_PORT = 27017
    # MONGODB_DBNAME = 'meishijie'
    # MONGODB_CNAME = 'meishi'
    # client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    # mydb = client[MONGODB_DBNAME]
    # post = mydb[MONGODB_CNAME]
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    title_list = ['菜名', '菜谱url', '图片', '视频', '工艺', '口味', '时间',
                  '难度', '饭量（人份）', '高血脂人群', '减肥人群', '高血压人群',
                  '高血糖人群', '儿童', '糖（克）',
                  '热量（大卡）', '脂肪（克）', '主料', '辅料', '步骤']
    all_list = [title_list]
    # get_list()

    get_detail('https://www.meishij.net/zuofa/yumimianbao_10.html')
    # df = pd.DataFrame(all_list)
    # df.to_excel('text.xlsx')
    # get_list()
    # get_two()
