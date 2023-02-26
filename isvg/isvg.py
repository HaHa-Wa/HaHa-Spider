# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/25 10:58 下午
@Auth ： HaHa-Wa
@File ：isvg.py
@IDE ：PyCharm
"""
import time

import requests
import pandas as pd
from io import BytesIO

import retrying
from PIL import Image
from pyzbar.pyzbar import decode
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


@retrying.retry(stop_max_attempt_number=10, wait_fixed=2000)
def send_q(url):
    ret = requests.get(url, headers=headers, timeout=3)
    return ret


def download_img(url):
    ret = send_q(url)
    file_name = url[url.rfind('/') + 1:]
    print(file_name)
    with open(f'img/{file_name}', 'wb')as f:
        f.write(ret.content)
    return file_name


def get_img(url):
    response = send_q(url)
    # 将图片数据转换为文件对象
    image_file = BytesIO(response.content)
    image = Image.open(image_file)

    # 将图片转换为 RGBA 模式，方便对透明度进行处理
    image = image.convert("RGBA")
    # 获取图片的大小
    width, height = image.size
    # 创建一个白色背景的图片
    background = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    # 将原图片粘贴到白色背景上
    background.paste(image, (0, 0), image)
    # 将背景变为纯白色，将 alpha 通道设置为不透明
    background = background.convert("RGB")
    # 解码二维码
    decoded_data = decode(background)
    # 打印解码结果
    if decoded_data:
        return decoded_data[0].data.decode('utf-8')
    else:
        print('无法解码二维码')


def get_info(url):
    res = send_q(url)
    bs_ret = BeautifulSoup(res.text, 'lxml')
    t_info = bs_ret.find('h1', class_='c-heading heading_IofCsr').text.replace('| ', '｜').split('｜')
    title = t_info[0]
    technology = t_info[1]
    account = t_info[2]
    div_s = bs_ret.find_all('p', class_='paragraph_8Ww9OP')
    introduction = div_s[0].text
    date_time = div_s[1].text
    contact = div_s[2].text
    img_src = 'https:' + bs_ret.find('img', class_='c-image image_NKedk4')['src']
    image_GYZi4V = 'https:' + bs_ret.find('img', class_='c-image image_GYZi4V')['src']
    file_name_img = download_img(img_src)
    # file_name_img = ''
    wechat_href = get_img(image_GYZi4V)
    print(title, account)
    all_list.append([title, account, wechat_href, file_name_img, img_src, introduction, technology, date_time, contact])


def search():
    page = 1
    while True:
        # url = f'https://www.isvg.com/search/keywords!!{keyword}/?page={page}&list_id=contentgridviewv2_8d05d92c'
        url = f'https://www.isvg.com/?page={page}&list_id=contentgridviewv2_8d05d92c'
        ret = send_q(url)
        bs_ret = BeautifulSoup(ret.text, 'lxml')
        div_main = bs_ret.find('div', class_='row c-row row_myOKWH')
        a_s = div_main.find_all('a', class_='c-textlink textlink_m9g942')
        for a_ in a_s:
            de_href = 'https://www.isvg.com/' + a_['href']
            get_info(de_href)
        max_page = bs_ret.find_all('a', class_='c-paginationlink paginationlink_IAZedw')[-1].text.strip()
        print(max_page)
        if page == int(max_page):
            break
        page += 1


if __name__ == '__main__':
    T_list = ['标题', '账号', '链接', '图片名', '图片链接', '备注', '技术', '发布时间', '联系方式']
    all_list = [T_list]
    # keyword = input('输入关键词:')
    keyword = ''
    try:
        search()
    except:
        print('中途停止。。')

    df_filename = keyword+str(time.time())+'.xlsx'
    df = pd.DataFrame(all_list)
    df.to_excel(df_filename, index=False)
