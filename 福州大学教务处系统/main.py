import json

import pymongo
import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'jwch.fzu.edu.cn',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}


# 创建数据库类 连接本地数据库
class Mongo:

    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)  # 创建链接
        # 连接所需数据库名
        db = client['data']
        # 连接对应的库表
        self.post = db['fuzhou']

    # 插入一条数据
    def insert_one(self, item):
        postItem = dict(item)  # 转化为字典形式
        self.post.insert_one(postItem)  # 向表中插入一条数据
        return item  # 可以输出到控制台,可以不写

    # 插入多条数据
    def insert_many(self, item_list):
        self.post.insert_many(item_list)  # 向表中插入多条数据
        return item_list  # 可以输出到控制台,可以不写


def get_d_file_num(wbnewsid):
    params = {
        'wbnewsid': wbnewsid,
        'owner': '1744984858',
        'type': 'wbnewsfile',
        'randomid': 'nattach',
    }

    response = requests.get('https://jwch.fzu.edu.cn/system/resource/code/news/click/clicktimes.jsp', params=params,
                            headers=headers)
    return json.loads(response.content.decode())['wbshowtimes']


def down_file(file_path, file_name):
    base_url = 'https://jwch.fzu.edu.cn/' + file_path
    file_res = requests.get(base_url, headers=headers)
    with open('file/%s' % file_name, 'ab')as f:
        f.write(file_res.content)
        f.close()


def get_detail(url):
    res = requests.get(url, headers=headers)
    bs_detail = BeautifulSoup(res.content.decode(), 'lxml')
    content = bs_detail.find('div', {'class': 'xl_main'})
    file_list = content.find_all('li')
    file_info = []
    for info in file_list:
        file_path = info.a['href']
        file_name = info.a.text[4:].replace('\u200b', '')
        d_id = info.span['id']
        d_num = get_d_file_num(d_id.replace('nattach', ''))
        down_file(file_path, file_name)
        file_info.append({
            "file_path": file_path,
            "file_name": file_name,
            "d_num": d_num,
        })
    return (file_info, str(content))


def main():
    i = True

    for page in range(174, 154, -1):
        response = requests.get('https://jwch.fzu.edu.cn/jxtz/{0}.htm'.format(page), headers=headers)

        bs_html = BeautifulSoup(response.content.decode(), 'lxml')
        if i:
            page_num = bs_html.find_all('span', {'class': 'p_no'})[-1].text
            print('共计：{0}页'.format(page_num))

            i = False
        list_li = bs_html.find('ul', {"class": 'list-gl'}).find_all('li')
        news_list = []

        for x in list_li:
            li_info = x.text.strip().replace('\r', '').split('\n')
            date_info = li_info[0]
            infrom = li_info[1].replace(' ', '').replace('【', '').replace('】', '')
            title = li_info[2].replace(' ', '')
            href = 'https://jwch.fzu.edu.cn/' + x.find('a')['href'][2:]
            file_info, content = get_detail(href)

            news_list.append({
                "date_info": date_info,
                "infrom": infrom,
                "title": title,
                "href": href,
                'file_info': file_info,
                'content': content
            })

        mongo_client.insert_many(news_list)
        print(news_list)


if __name__ == '__main__':
    mongo_client = Mongo()
    main()
