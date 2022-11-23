import json
import time

import requests
import xlwt
from bs4 import BeautifulSoup


# 存入excel  时间命名
from pip._vendor.retrying import retry


def processing_data(content_list):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('上海小区名单')

    # 写入excel
    # 参数对应 行, 列, 值
    for i, content in enumerate(content_list):
        for x, info in enumerate(content):
            worksheet.write(i, x, label=info)  # 将数据存入excel

    # 保存
    workbook.save('上海小区名单.xls')

@retry(stop_max_attempt_number=10, wait_fixed=2000)
def getxiaoquaddress(id):
    url = 'https://sh.lianjia.com/xiaoqu/%s/' % id

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
    }
    res = requests.get(url, headers=headers, timeout=3)
    ret = BeautifulSoup(res.text, 'lxml')
    address = ret.find('div', class_='detailDesc')
    return address.text


if __name__ == '__main__':
    all_xiaoqu = [['ID', '小区名称', '区', '镇', '详细地址', '线上链接']]
    with open('shxiaoqu.json', 'r') as f:
        shzhen = json.load(f)
    for x in shzhen:
        print(x)
        try:
            address = getxiaoquaddress(x['id'])
        except:
            with open('shxiaoqu_detail.json', 'w') as fp:  # path为json文件路径
                json.dump(all_xiaoqu, fp, indent=4, ensure_ascii=False)

            processing_data(all_xiaoqu)
        print(address)
        all_xiaoqu.append([
            x['id'],
            x['name'],
            x['districtName'],
            x['bizcircleName'],
            address,
            x['viewUrl']
        ])
        # time.sleep(0.2)
        # break
    with open('shxiaoqu_detail.json', 'w') as fp:  # path为json文件路径
        json.dump(all_xiaoqu, fp, indent=4, ensure_ascii=False)

    processing_data(all_xiaoqu)
