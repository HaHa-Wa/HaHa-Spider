import json
import time

import requests
from bs4 import BeautifulSoup
all_xiaoqu = []
qu_list = [
    {'qu_name': '浦东', 'qu_href': 'https://sh.lianjia.com/xiaoqu/pudong/'},
    {'qu_name': '闵行', 'qu_href': 'https://sh.lianjia.com/xiaoqu/minhang/'},
    {'qu_name': '宝山', 'qu_href': 'https://sh.lianjia.com/xiaoqu/baoshan/'},
    {'qu_name': '徐汇', 'qu_href': 'https://sh.lianjia.com/xiaoqu/xuhui/'},
    {'qu_name': '普陀', 'qu_href': 'https://sh.lianjia.com/xiaoqu/putuo/'},
    {'qu_name': '杨浦', 'qu_href': 'https://sh.lianjia.com/xiaoqu/yangpu/'},
    {'qu_name': '长宁', 'qu_href': 'https://sh.lianjia.com/xiaoqu/changning/'},
    {'qu_name': '松江', 'qu_href': 'https://sh.lianjia.com/xiaoqu/songjiang/'},
    {'qu_name': '嘉定', 'qu_href': 'https://sh.lianjia.com/xiaoqu/jiading/'},
    {'qu_name': '黄浦', 'qu_href': 'https://sh.lianjia.com/xiaoqu/huangpu/'},
    {'qu_name': '静安', 'qu_href': 'https://sh.lianjia.com/xiaoqu/jingan/'},
    {'qu_name': '虹口', 'qu_href': 'https://sh.lianjia.com/xiaoqu/hongkou/'},
    {'qu_name': '青浦', 'qu_href': 'https://sh.lianjia.com/xiaoqu/qingpu/'},
    {'qu_name': '奉贤', 'qu_href': 'https://sh.lianjia.com/xiaoqu/fengxian/'},
    {'qu_name': '金山', 'qu_href': 'https://sh.lianjia.com/xiaoqu/jinshan/'},
    {'qu_name': '崇明', 'qu_href': 'https://sh.lianjia.com/xiaoqu/chongming/'}
]


def community_list(xiaoqu):
    pg = 1
    while True:
        url = 'https://sh.lianjia.com/xiaoqu/%s/pg%s/' % (xiaoqu, pg)
        print(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        ret = requests.get(url, headers=headers)
        bs_ret = BeautifulSoup(ret.text, 'lxml')
        bs_ul = bs_ret.find('ul', class_='listContent')
        if not bs_ul:
            break
        bs_lis = bs_ul.find_all('li', class_='clear xiaoquListItem')

        print(len(bs_lis))
        if len(bs_lis) < 29:
            break
        pg += 1


def community_list_m(xiaoqu):
    pg = 1
    while True:
        url = 'https://m.lianjia.com/liverpool/api/webApiProxy/secondhand/resblock/search?'
        params = {
            'cityId': 310000,
            'condition': '/%s/pg%s' % (xiaoqu, pg),
            'curPage': pg
        }
        print(url)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
        }

        ret = requests.get(url, headers=headers, params=params)
        res = ret.json()
        data_list = res['data']['data']['list']
        all_xiaoqu.extend(data_list)

        if len(data_list) < 29:
            break
        pg += 1


def get_qu():
    url = 'https://sh.lianjia.com/xiaoqu/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    ret = requests.get(url, headers=headers).text
    bs_ret = BeautifulSoup(ret, 'lxml').find('div', {"data-role": 'ershoufang'}).find('div').find_all('a')
    qu_list = []
    for x in bs_ret:
        # print(x)
        qu_href = x['href']
        qu_name = x.text
        # print(qu_name, qu_href)
        qu_list.append({
            'qu_name': qu_name, 'qu_href': 'https://sh.lianjia.com'+qu_href
        })
    return qu_list[:-1]


def get_zhen(qu):
    url = qu['qu_href']

    ret = requests.get(url, headers=headers).text
    bs_ret = BeautifulSoup(ret, 'lxml').find('div', {"data-role": 'ershoufang'}).find_all('div')[1].find_all('a')
    for x in bs_ret:
        # print(x)
        zhen_href = x['href']
        zhen_name = x.text
        # print(qu_name, qu_href)
        zhen_list.append({
            'qu_name': qu['qu_name'], 'qu_href': qu['qu_href'],
            'zhen_name': zhen_name, 'zhen_href': zhen_href.replace('/xiaoqu/', ''). replace('/', '')
        })


if __name__ == '__main__':

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    # 获取所有镇
    # zhen_list = []
    #
    # for x in get_qu():
    #     print(x)
    #     get_zhen(x)
    #     time.sleep(1)
    #
    # with open('shzhen.json', 'w', encoding='utf-8') as fp:  # path为json文件路径
    #     json.dump(zhen_list, fp, indent=4)
    with open('shzhen.json', 'r') as f:
        shzhen = json.load(f)
    print(shzhen)
    for x in shzhen:

        community_list_m(x['zhen_href'])
        # break
    # print(all_xiaoqu)
    print(len(all_xiaoqu))
    with open('shxiaoqu.json', 'w') as fp:  # path为json文件路径
        json.dump(all_xiaoqu, fp, indent=4, ensure_ascii=False)
