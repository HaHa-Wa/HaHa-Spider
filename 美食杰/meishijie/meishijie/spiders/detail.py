import numpy
import scrapy
from bs4 import BeautifulSoup
from pymongo import MongoClient
from meishijie.items import MeishijieItem
from meishijie.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME


class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['meishij.net']
    start_urls = ['http://meishij.net/']
    # https://www.meishij.net/zuofa/shengdanshudangao.html
    def start_requests(self):
        all_href = find_info()
        ssss = False
        for info in all_href:
            href = info['href']
            tag = info['tag']
            if href == 'https://www.meishij.net/zuofa/shengdanshudangao.html':
                ssss = True
            if ssss:
                yield scrapy.Request(url=href, callback=self.parse, meta={'tag': tag, 'href': href})

    def parse(self, response):
        ret = response.body
        meta = response.meta
        tag = meta['tag']
        href = meta['href']
        bs_ret = BeautifulSoup(ret, 'lxml')
        one_list = parse_detail(bs_ret, href)
        item = MeishijieItem()
        item['title'] = one_list[0]
        item['tag'] = ','.join(tag)
        item['url'] = one_list[1]
        item['recipe_topimg'] = one_list[2]
        item['recipe_topvideo'] = one_list[3]
        item['gongyi'] = one_list[4]
        item['kouwei'] = one_list[5]
        item['shijian'] = one_list[6]
        item['nandu'] = one_list[7]
        item['fanliang'] = one_list[8]
        item['gaoxiezhi'] = one_list[9]
        item['jianfei'] = one_list[10]
        item['gaoxieya'] = one_list[11]
        item['gaoxietang'] = one_list[12]
        item['ertong'] = one_list[13]
        item['tang'] = one_list[14]
        item['reliang'] = one_list[15]
        item['zhifang'] = one_list[16]
        item['zhuliao'] = one_list[17]
        item['fuliao'] = one_list[18]
        item['recipe_step_box'] = one_list[19]
        item['step_box'] = one_list[20]
        yield item


def find_info():
    client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    # 连接数据库
    mydb = client[MONGODB_DBNAME]
    post2 = mydb['meishi2']
    ret = list(post2.find())
    return ret


def parse_detail(bs_ret, url):
    recipe_step_box = bs_ret.find('div', class_='recipe_step_box')
    title = bs_ret.find('h1', class_='recipe_title').text
    try:
        gongyi = bs_ret.find('div', class_='info2_item info2_item1').find('strong').text
    except:
        gongyi = numpy.nan
    try:
        kouwei = bs_ret.find('div', class_='info2_item info2_item2').find('strong').text
    except:
        kouwei = numpy.nan
    try:
        shijian = bs_ret.find('div', class_='info2_item info2_item3').find('strong').text
    except:
        shijian = numpy.nan
    try:
        nandu = bs_ret.find('div', class_='info2_item info2_item4').find('strong').text
    except:
        nandu = numpy.nan
    try:
        recipe_topimg = bs_ret.find('img', class_='recipe_topimg')['src']
        recipe_topvideo = numpy.nan
    except:
        recipe_topimg = bs_ret.find('img', class_='recipe_topvideo_bg')['src']
        recipe_topvideo = bs_ret.find('video', id='main_video')['src']
    try:
        zhuliao = bs_ret.find('div', class_='recipe_ingredients').find('div', class_='right')
        zhuliao = get_zhuliao(zhuliao)
    except:
        zhuliao = numpy.nan
    try:
        fuliao = bs_ret.find('div', class_='recipe_ingredients recipe_ingredients1').find('div', class_='right')
        fuliao = get_zhuliao(fuliao)
    except:
        fuliao = numpy.nan
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

    # if fitme_items:
    try:
        fanliang = bs_ret.find('span', class_='rf').text.replace('人份', '')
    except:
        fanliang = numpy.nan
    try:
        fitme_items = bs_ret.find('div', class_='fitme_items')
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
                tang, reliang, zhifang, str(zhuliao), str(fuliao), str(recipe_step_box), step_box]
    return one_list


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


def get_zhuliao(ret):
    z_dict = {}
    strongs = ret.find_all('strong')
    for st in strongs:
        a = st.find('a').text
        v = st.text.replace(a, '')
        z_dict[a] = v
    return z_dict
