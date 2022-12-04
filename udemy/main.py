import json
import os
import time

import requests


def convert_cookies_to_dict(cookies):
    cookies = dict([l.split("=", 1) for l in cookies.split("; ")])
    return cookies


def download_file(href, filename, path2):
    path2 = path2.replace('/', '-')
    if not os.path.exists(f'{file_path}/{path2}'):  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(f'{file_path}/{path2}')  # makedirs 创建文件时如果路径不存在会创建这个路径
    ret = requests.get(url=href, headers=headers)
    with open(f"{file_path}/{path2}/{filename}", 'wb')as f:
        f.write(ret.content)


def get_mp4(ID2, fileName, path2):
    body = {
        'ID': ID,
        'ID2': ID2,
        'cookie': json.dumps(cookie)
    }
    url = 'http://127.0.0.1:16060/get_mp4'
    ret = requests.get(url, headers=headers, params=body)
    mp4_info = ret.json()
    try:
        asset = mp4_info['data']['asset']
    except:
        print(mp4_info)
    captions = asset['captions'][2]
    download_url = asset['media_sources'][0]['src']
    download_file(download_url, fileName, path2)
    caption_name = captions['title']
    caption_href = captions['url']
    download_file(caption_href, caption_name, path2)
    time.sleep(3)


def get_mp4_list():
    url = 'http://127.0.0.1:16060/get_mp4_list'

    body = {
        'ID': ID,
        'cookie': json.dumps(cookie)
    }
    try:
        ret = requests.get(url, headers=headers, params=body)
    except:
        print('重启node服务后使用')

    mp4_list = ret.json()['data']['results']
    with open('mp4List.json', 'w')as f:
        json.dump(ret.json(), f)
    path2 = ''
    for mp4 in mp4_list:
        if mp4['_class'] == 'lecture':
            if mp4['asset']['asset_type'] == 'Video':
                asset = mp4['asset']
                filename = asset['filename']
                ID2 = mp4['id']
                get_mp4(ID2, filename, path2)
                print(f'视频{filename} 下载成功。。')
        else:
            path2 = mp4['title']


if __name__ == '__main__':
    # ID = 593108
    # file_path = 'test'

    ID = input('请输入视频ID：')
    file_path = input('输入文件夹名：')
    with open('cookie.txt', 'r')as f:
        cookie_txt = f.read()
    cookie = convert_cookies_to_dict(cookie_txt.replace('\n', ''))
    cookie['ud_last_auth_information'] = ''
    cookie['OptanonConsent'] = ''
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    get_mp4_list()
