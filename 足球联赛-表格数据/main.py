# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/5 3:42 下午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    # 遍历球队
    for ballgame, key in ballgame_dict.items():
        # 设置url
        url = 'http://www.tzuqiu.cc/competitions/%s/teamStats.do'%key
        # 设置请求头
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        }
        # 发送请求 获取原始数据
        ret = requests.get(url=url, headers=headers)
        res = ret.content.decode()
        # 解析数据
        bs_ret = BeautifulSoup(res, 'lxml')
        # 取出html数据
        divs = bs_ret.find_all('div', class_='tab-content')[1]
        # 再次定位 取出精确表格
        table_divs = divs.find_all('div')
        # 取出进攻数据
        attack = table_divs[1]
        # 取出组织数据
        organization = table_divs[3]
        # 利用pandas 将html格式表格转换为excel格式
        organization_pd = pd.read_html(str(organization))[0]
        attack_pd = pd.read_html(str(attack))[0]
        # 打开要写入的excel
        writer = pd.ExcelWriter('%s.xlsx'%ballgame)
        # 将数据写入不同的sheet
        organization_pd.to_excel(writer, encoding='utf-8', sheet_name='组织')
        attack_pd.to_excel(writer, encoding='utf-8', sheet_name='进攻')
        # 保存excel
        writer.save()


if __name__ == '__main__':
    ballgame_dict = {
        '德甲': '4',
        '英超': '1',
        '西甲': '2',
        '法甲': '6',
        '意甲': '5',
    }
    main()
