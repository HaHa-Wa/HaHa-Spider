# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/8 10:02 上午
@Auth ： HaHa-Wa
@File ：main.py
@IDE ：PyCharm
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_list():
    all_info = []
    for page in range(1, 6):
        params = {
            'Drpcallist': '',
            'Drpseclist': '',
            'allwords': 'شينجيانغ',
            'page': str(page),
        }

        data = {
            'allwords': 'شينجيانغ',
        }
        response = requests.post('https://www.youm7.com/home/Search', params=params, cookies=cookies, headers=headers,
                                 data=data)
        bs_ret = BeautifulSoup(response.text, 'lxml')
        news_item = bs_ret.find_all('div', class_='info_section news-item')
        for item in news_item:
            # print(item)
            h2_a = item.find('h2').find('a')
            title = h2_a.text
            href = 'https://www.youm7.com' + h2_a['href']
            date_time = item.find('h3').text
            detail = get_detail(href)
            print(title)
            print(href)
            all_info.append([title, date_time, detail, href])
    df = pd.DataFrame(all_info)
    df.to_excel('youm7.xlsx')


def get_detail(href):
    response = requests.post(url=href, cookies=cookies, headers=headers)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    articleBody = bs_ret.find('div', id='articleBody')
    print(articleBody.text)
    return articleBody.text

if __name__ == '__main__':
    cookies = {
        '_gid': 'GA1.2.1523779417.1675820292',
        'Location': 'Indonesia',
        'FooterLoc': 'Indonesia',
        '_pbjs_userid_consent_data': '3524755945110770',
        '_pubcid': 'ce9e350e-71fb-48db-bdd1-ebcaeea9eb15',
        '__gpi': 'UID=00000bb7a47903b8:T=1675820294:RT=1675820294:S=ALNI_MYCoS4VV5yN-IDo4jTjXtqSffrGjw',
        'cto_bidid': 'OEh7PF9LMDJCaFM5TkFLd1BBZ0ZMQ1lRZEx3MTNkZnUlMkZyWUozZGVnbEhkOTFxR1BIT3pCczUzVGFCQXhINzk5QU41czNDd3k3RGdsYzJqYWVnRjhXUEtMVFowQW1Nc0Rlc0NzdiUyRlBLNEd0SDlIUU0lM0Q',
        'cto_bundle': 'lmixCl80VWdVY3RGWkF6YVBjV1ZxV2xqc3ZtN2FzTktKVU14elJkN3ZBN1VsYmpSUlRxU0t5aU9vMSUyRmJtMkpvTmhQYUVUUFg5S0pqS1JQVlR4Q2hiOXZnSTJXOThPVDhDWSUyRlBRV2VrZVBPSWx0Y0xsRXd2MndpRG1sbmZhWiUyRjV4VmYlMkZRcWV4bW1tYTc3NEQlMkZtOE50S2w3dmNRJTNEJTNE',
        '__gads': 'ID=ae5df6d0da67c683-225dd07992d90042:T=1675820294:S=ALNI_MajgGwYa1y4ojHD111y9xLQdTomsg',
        '_ga': 'GA1.2.983657366.1675820292',
        '__asc': 'e14b7f701862eafc10c575ce26a',
        '__auc': 'e14b7f701862eafc10c575ce26a',
        '_ga_J7S2SZJ3N7': 'GS1.1.1675820291.1.1.1675821678.0.0.0',
    }

    headers = {
        'authority': 'www.youm7.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        # 'cookie': '_gid=GA1.2.1523779417.1675820292; Location=Indonesia; FooterLoc=Indonesia; _pbjs_userid_consent_data=3524755945110770; _pubcid=ce9e350e-71fb-48db-bdd1-ebcaeea9eb15; __gpi=UID=00000bb7a47903b8:T=1675820294:RT=1675820294:S=ALNI_MYCoS4VV5yN-IDo4jTjXtqSffrGjw; cto_bidid=OEh7PF9LMDJCaFM5TkFLd1BBZ0ZMQ1lRZEx3MTNkZnUlMkZyWUozZGVnbEhkOTFxR1BIT3pCczUzVGFCQXhINzk5QU41czNDd3k3RGdsYzJqYWVnRjhXUEtMVFowQW1Nc0Rlc0NzdiUyRlBLNEd0SDlIUU0lM0Q; cto_bundle=lmixCl80VWdVY3RGWkF6YVBjV1ZxV2xqc3ZtN2FzTktKVU14elJkN3ZBN1VsYmpSUlRxU0t5aU9vMSUyRmJtMkpvTmhQYUVUUFg5S0pqS1JQVlR4Q2hiOXZnSTJXOThPVDhDWSUyRlBRV2VrZVBPSWx0Y0xsRXd2MndpRG1sbmZhWiUyRjV4VmYlMkZRcWV4bW1tYTc3NEQlMkZtOE50S2w3dmNRJTNEJTNE; __gads=ID=ae5df6d0da67c683-225dd07992d90042:T=1675820294:S=ALNI_MajgGwYa1y4ojHD111y9xLQdTomsg; _ga=GA1.2.983657366.1675820292; __asc=e14b7f701862eafc10c575ce26a; __auc=e14b7f701862eafc10c575ce26a; _ga_J7S2SZJ3N7=GS1.1.1675820291.1.1.1675821678.0.0.0',
        'origin': 'https://www.youm7.com',
        'pragma': 'no-cache',
        'referer': 'https://www.youm7.com/home/Search?Drpcallist=&Drpseclist=&allwords=%D8%B4%D9%8A%D9%86%D8%AC%D9%8A%D8%A7%D9%86%D8%BA&page=2',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    # get_detail()
    get_list()
