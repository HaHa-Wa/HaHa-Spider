# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/11 11:07 下午
@Auth ： HaHa-Wa
@File ：影视信息.py
@IDE ：PyCharm
"""
import pymongo
import requests
from bs4 import BeautifulSoup
import retrying

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


def get_session_list(url):
    # url = 'https://myflixer.to/ajax/v2/season/episodes/73618'
    bs_ret = send_req(url)

    lis = bs_ret.find_all('li', class_='nav-item')
    title_list = []
    for li in lis:
        a_ = li.find('a')
        title = a_['title']
        # print(title)
        title_list.append(title)
    return title_list


def get_info(mv_id):
    url = 'https://myflixer.to/ajax/v2/tv/seasons/' + str(mv_id)
    bs_ret = send_req(url)
    id_divs = bs_ret.find_all('a', class_='dropdown-item ss-item')
    all_juji = []
    for div in id_divs:
        href = 'https://myflixer.to/ajax/v2/season/episodes/' + div['data-id']
        juji = div.text
        title_list = get_session_list(href)
        all_juji.append({
            juji: title_list
        })
    return all_juji


@retrying.retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_req(url):
    ret = requests.get(url, headers=headers, timeout=5)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    return bs_ret


def get_detail(title, href):
    # href = 'https://myflixer.to/tv/interrupting-chicken-90355'
    bs_ret = send_req(href)

    detail_page = bs_ret.find('div', class_='detail_page-infor')
    pingfen = detail_page.find('button', class_='btn btn-sm btn-radius btn-warning btn-imdb').text
    description = detail_page.find('div', class_='description').text
    # print(pingfen, description)
    elements = detail_page.find('div', class_='elements')
    # print(elements)
    row_line = elements.find_all('div', class_='row-line')
    Released = row_line[0].text.replace('   ', '').replace('\n', '')
    Genre = row_line[1].text.replace('   ', '').replace('\n', '')
    Duration = row_line[2].text.replace('   ', '').replace('\n', '')
    Country = row_line[3].text.replace('   ', '').replace('\n', '')
    Production = row_line[4].text.replace('   ', '').replace('\n', '')
    Casts = row_line[5].text.replace('   ', '').replace('\n', '')
    # print(Released, Genre, Duration, Country, Production, Casts)
    mv_id = href[href.rfind('-') + 1:]
    all_juji = get_info(mv_id)
    item_mongo = {
        'title': title,
        'pingfen': pingfen,
        'mv_id': mv_id,
        'description': description,
        'Released': Released,
        'Genre': Genre,
        'Duration': Duration,
        'Country': Country,
        'Production': Production,
        'Casts': Casts,
        'href': href,
        'all_juji': all_juji,
    }
    insert(item_mongo)


def insert(item):
    post.insert_one(item)


def get_list():
    for page in range(32, 369):
        print('page:  ', page)
        url = 'https://myflixer.to/genre/animation?page={0}'.format(page)

        bs_ret = send_req(url)

        film_list_wrap = bs_ret.find('div', class_='film_list-wrap')
        flw_item = film_list_wrap.find_all('div', class_='flw-item')
        for item in flw_item:
            # print(item)
            h2 = item.find('h2', class_='film-name').find('a')
            title = h2['title']
            href = 'https://myflixer.to' + h2['href']
            print(title, href)
            if title == '0号宿舍':
                continue
            get_detail(title, href)


if __name__ == '__main__':
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DBNAME = 'myflixer'
    MONGODB_CNAME = 'tv'
    client = pymongo.MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    mydb = client[MONGODB_DBNAME]
    post = mydb[MONGODB_CNAME]
    get_list()
    # get_detail()
    # gets_info()
    # get_session_list()
