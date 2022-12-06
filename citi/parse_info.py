import json
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_comInfo():
    import requests

    cookies = {
        'qgqp_b_id': 'ce3ad283737840e8de449b5f90871caa',
        'st_si': '95850957570435',
        'st_asi': 'delete',
        'HAList': 'ty-0-300059-%u4E1C%u65B9%u8D22%u5BCC',
        'st_pvi': '58229334464610',
        'st_sp': '2022-11-23%2014%3A41%3A05',
        'st_inirUrl': 'https%3A%2F%2Fwww.google.com%2F',
        'st_sn': '9',
        'st_psi': '20221205224018376-113200301321-7569226325',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        # 'Cookie': 'qgqp_b_id=ce3ad283737840e8de449b5f90871caa; st_si=95850957570435; st_asi=delete; HAList=ty-0-300059-%u4E1C%u65B9%u8D22%u5BCC; st_pvi=58229334464610; st_sp=2022-11-23%2014%3A41%3A05; st_inirUrl=https%3A%2F%2Fwww.google.com%2F; st_sn=9; st_psi=20221205224018376-113200301321-7569226325',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://quote.eastmoney.com/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }


    com_list = []
    for page in range(1, 261):
        print('page:', page)
        response = requests.get(
            'http://79.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112406142875913978307_1670251217098&pn='+str(page)+'&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1670251217104',
            cookies=cookies,
            headers=headers,
            verify=False,
        )
        ret = response.text
        # print(ret)
        bs_ret = json.loads(ret[ret.find('(')+1:-2])['data']
        # trs = bs_ret.find_all('tr')
        print(bs_ret)
        # break
        for tr in bs_ret['diff']:
            name = tr['f12']
            code = tr['f14']
            print(name, code)
            com_list.append([name, code])
        time.sleep(1)
    new_df = pd.DataFrame(com_list)
    new_df.to_excel(f'com.xls')


def read_com():
    com_list = pd.read_excel('com.xls')
    print(com_list)
    # for x in com_list.values:
    #     print(x[1])
    return com_list


def read_excel(ID):
    com_list = read_com()
    com_info = [['公司', '分数', 'code', '公司股票']]
    df = pd.read_excel(f'excel_info/{ID}.xlsx')
    for x in df.values:
        try:
            x0 = x[0].replace('[', '').replace(']', '')
        except:
            x0 = ''
        try:
            x1 = x[1].replace('[', '').replace(']', '')
        except:
            x1 = 0
        ii = [x0, x1]
        for com in com_list.values:
            # try:
            print(x[0])
            if type(x[0]) == 'float':
                continue
            try:
                if x[0] in com[1]:
                    ii.append(com[0])
                    ii.append(com[1])
                    break
            except:
                continue
        com_info.append(ii)

    new_df = pd.DataFrame(com_info)
    new_df.to_excel(f'new_excel/{ID}.xls')


if __name__ == '__main__':
    # read_com()
    read_excel(2022)
    # get_comInfo()
    # ret = read_com()
    # print(ret)
    # new_df = pd.DataFrame(ret)
    # new_df.to_excel(f'com.xls')
