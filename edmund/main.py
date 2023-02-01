# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/26 4:50 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import re
import requests
import pandas as pd
from retrying import retry
from bs4 import BeautifulSoup


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_detail_two(title, productFamilyID):
    params = (
        ('productFamilyID', productFamilyID),
        ('isPreviewMode', 'false'),
        ('_', '1674808927614'),
    )

    response = requests.get('https://www.edmundoptics.cn/Catalog/ProductFamily/_Accessories/', headers=headers,
                            params=params, timeout=5)
    tables = pd.read_html(response.text)
    tables_df = tables[0]
    for info in tables_df.itertuples():
        try:
            p_code = info[-3].replace('#', '')
            price = info[-2][:info[-2].find('数量')].replace(' 索取报', '').replace('RMB ', '').replace(' ', '').replace(',',
                                                                                                                    '')
            print(title, productFamilyID, p_code, float(price))
            all_info.append([title, p_code, float(price)])
        except:
            pass


def get_detail(title, SchemaId, productFamilyID):
    params = (
        ('productFamilyID', str(productFamilyID)),
        ('schemaID', str(SchemaId)),
        ('IsHiddenGridSpecs', 'False'),
        ('previewCode', ''),
        ('IsPreviewMode', 'False'),
        ('resetCache', 'false'),
        ('filterSelections', ''),
        ('_', '1674748798683'),
    )
    url = 'https://www.edmundoptics.cn/Catalog/ProductFamily/_ProductGrid/'
    response = requests.get(url, headers=headers, params=params)
    try:
        tables = pd.read_html(response.text)
    except:
        get_detail_two(title, productFamilyID)
        return
    tables_df = tables[0]
    for info in tables_df.itertuples():
        try:
            p_code = info[-3].replace('#', '')
            price = info[-2][:info[-2].find('数量')].replace(' 索取报', '').replace('RMB ', '').replace(' ', '').replace(',',
                                                                                                                    '')
            print(title, SchemaId, productFamilyID, p_code, float(price))
            all_info.append([title, p_code, price])
        except:
            pass


@retry(stop_max_attempt_number=10, wait_fixed=2000)
def get_two(href):
    ret = requests.get(url=href, headers=headers, timeout=5)
    SchemaId = re.findall(r'SchemaId: (.*?),', ret.text)[0]
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    divs = bs_ret.find_all('div', class_='col-lg-3 col-md-6 col-6 product-family-result')
    for div in divs:
        # print(li)
        a_two = div.find_all('a')[1]
        title = a_two.text
        d_href = a_two['href']
        productFamilyID = d_href[d_href[:-1].rfind('/') + 1:-1]
        print(title, productFamilyID, SchemaId)
        get_detail(title, SchemaId, productFamilyID)


def get_megamenu():
    url = 'https://www.edmundoptics.cn/Catalog/Category/MegaMenu'
    ret = requests.get(url, headers=headers)
    bs_ret = BeautifulSoup(ret.text, 'lxml')
    a_s = bs_ret.find_all('a', class_='menu-link mm-optics-t1')
    all_category = {}
    for a_ in a_s:
        one_title = a_.text
        lis = a_.parent
        li_two = lis.find_all('a', class_='menu-link menu-list-link')
        two_href_list = []
        for onea in li_two:
            two_title = onea.text
            href = "https://www.edmundoptics.cn" + onea['href']
            two_href_list.append([two_title, href])

        li_two_ = lis.find_all('a', class_='menu-link menu-bar-link')
        for onea in li_two_[:-1]:
            two_title = onea.text
            href = "https://www.edmundoptics.cn" + onea['href']
            two_href_list.append([two_title, href])

        all_category[one_title] = two_href_list
    # print(all_category)
    sP = ['光学件']
    for category, href_list in all_category.items():
        if category in sP:
            for x in href_list:
                # print(x)
                get_two(x[1])
            # break
        # break


if __name__ == '__main__':
    all_info = [['name', 'p_code', 'price']]
    headers = {
        'authority': 'www.edmundoptics.cn',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.edmundoptics.cn/f/ultrafast-thin-plano-convex-lenses/39517/',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    try:
        get_megamenu()
    except:
        print('网络原因，采集失败。。。。')
    # get_two('https://www.edmundoptics.cn/c/schott/1311/')
    df = pd.DataFrame(all_info)
    df.to_excel('edmund.xlsx')
