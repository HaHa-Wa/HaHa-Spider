import requests
from bs4 import BeautifulSoup
import time


def dowload_img(href):
    ret = requests.get(href, headers=headers)
    file_name = str(time.time()).replace('.', '') + href[href.rfind('.'):]
    with open(f'file/{file_name}', 'wb')as f:
        f.write(ret.content)


def main(url):
    res = requests.get(url, headers=headers)
    bs_ret = BeautifulSoup(res.content.decode(), 'lxml')
    div = bs_ret.find('div', class_='css-79elbk')
    img_html_list = div.find_all('img')
    for img in img_html_list:
        href = img['src']
        print(href)
        if 'data:image/svg' not in href:
            dowload_img(href)
        # print(href[href.rfind('.'):])
        # break
    # print(img_html_list)


if __name__ == '__main__':
    # url = 'https://zhuanlan.zhihu.com/p/143853522'
    url_list = [
        'https://zhuanlan.zhihu.com/p/143198560',
        'https://zhuanlan.zhihu.com/p/142415613',
        'https://zhuanlan.zhihu.com/p/141875887'
    ]
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    for url in url_list:

        main(url)
    # print(str(time.time()).replace('.', ''))
