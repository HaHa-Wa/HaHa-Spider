import requests
import pandas as pd

from bs4 import BeautifulSoup


def get_detail(href, show_date, city):
    # url = 'http://www.jc.net.cn/net/eprice/material/MaterialAction.do?method=gotoMaterialDetail&pid=40352'
    ret = requests.get(href, headers)
    bs_ret = BeautifulSoup(ret.content.decode(), 'lxml')
    tr_list = bs_ret.find_all('tr', {'class': 'soli_content_tr'})
    for tr in tr_list:
        tds = tr.find_all('td')
        name = tds[0].text.strip()
        model = tds[1].text.strip()
        material = tds[2].text.strip()
        unit = tds[3].text.strip()
        unit_price = tds[4].text.strip()
        # print(name, model, material, unit, unit_price)
        print('类型：', name + model, '日期：', show_date ,'价格：', unit_price)
        if name + model not in content_dict:
            content_dict[name + model] = {"name": name, "model": model, "material": material, "unit": unit,
                                          "city": city,
                                          show_date: unit_price, }
        else:
            content_dict[name + model][show_date] = unit_price


def main():
    # 修改采集页数
    for page in range(1, 16):
        url = f'http://www.jc.net.cn/net/eprice/material/MaterialAction.do?method=gotoMaterialList&page={page}&area=11' # 地区ID

        ret = requests.get(url, headers)
        bs_ret = BeautifulSoup(ret.content.decode(), 'lxml')
        a_list = bs_ret.find_all('ul', {'class': 'solt_ul'})
        for x in a_list:
            title = x.find("li", {"class": 'solt_periods'})
            href = "http://www.jc.net.cn/" + title.find('a')['href']
            city = x.find('li', {'class': 'solt_area'}).text
            show_date = x.find('li', {"class": 'solt_reltime'}).text
            get_detail(href, show_date, city)


if __name__ == '__main__':
    content_dict = {}

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    main()
    data = pd.DataFrame(list(content_dict.values()))

    # 保存为csv格式
    data.to_csv('data.csv', encoding='utf-8')
    # get_detail()
    # print(content_dict)
