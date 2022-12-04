# -*- coding =utf-8 -*-
# @Time：2021/11/6 11:27
# @Author:Lila
# @File:All_Course.py

from bs4 import BeautifulSoup
from selenium import webdriver
from pandas import ExcelWriter
import pandas as pd

def getdata():
    driver = webdriver.Chrome()
    url='https://www.icourse163.org/search.htm?search=%E6%A6%82%E7%8E%87%E8%AE%BA%E4%B8%8E%E6%95%B0%E7%90%86%E7%BB%9F%E8%AE%A1#type=30&orderBy=0&pageIndex=1&courseTagType=null'#找出每一页的链接规律，定义格式，实现所有页面内容的爬取
    # head ={ #模拟浏览器的头部信息，向服务器发送消息
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    # } #用户代理，表示告诉服务器，我们是什么类型的机器，本质上是告诉浏览器，我们可以接收什么水平的文件
    # request=urllib.request.Request(url,headers=head)
    driver.get(url)
    response = driver.page_source  # 获得初始页面代码，接下来进行简单的解析
    soup = BeautifulSoup(response, 'html.parser')
    # print(soup)
    page = driver.find_element_by_class_name("ux-pager_btn__next")  # 翻页功能ux-pager_btn__next
    response = driver.page_source
    soup = BeautifulSoup(response, 'html.parser')

    global contlist
    contlist = []
    contlist.append(["课程名称", "标签", "授课学校", "授课老师", "参加人数","课程进度","课程简介"])
    for i in range(30):
        page.click()#实现翻页
        response = driver.page_source
        soup = BeautifulSoup(response, 'html.parser')
        all_content=soup.find_all('div',class_="u-clist f-bgw f-cb f-pr j-href ga-click")

        for cont in all_content:

            name = cont.find('span', class_="u-course-name f-thide")  # 爬出所有课程名称
            if name:
                name = name.get_text() # 把title转化成字符串
            else:
                name='-'
            # print(name)

            tag = cont.find('a', class_="tag u-course-tag f-f0 ga-click")  # 爬出所有课程标签,如果没有此标签则返回空值
            if tag:  # 判断tag是否为空值
                tag = tag.span.get_text()
            else:
                tag = '-'
            # print(tag)
            #
            univ = cont.fin
