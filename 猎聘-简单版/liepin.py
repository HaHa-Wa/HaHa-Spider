import time

import requests
import xlwt
from bs4 import BeautifulSoup


def processing_data(content_list):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('My Worksheet')
    # 写入excel
    for i, content in enumerate(content_list):
        for x, info in enumerate(content):
            worksheet.write(i, x, label=info)  # 将数据存入excel
    # 保存
    workbook.save(keyWord + '.xls')


def parse_info(bs_ret):
    # print(bs_ret)
    job_list = bs_ret.find('div', {'class': 'left-list-box'}).find('ul')
    # print(job_list[10])
    for job in job_list.find_all('li'):
        # print(job)
        jobInfo = job.find('div', {'class': 'job-detail-box'})
        title = jobInfo.find('div', {'class': 'job-title-box'}).text.strip().replace(' ', '').replace('\n', '')
        print(title)
        jobSalary = jobInfo.find('span', {'class': 'job-salary'}).text
        spans = jobInfo.find('div', {'class': 'job-labels-box'}).find_all('span')
        detailInfo_href = job.find('a', {'data-nick': 'job-detail-job-info'})['href']

        work_years = spans[0].text
        education = spans[1].text
        time.sleep(1)
        jd = parseDetal(detailInfo_href)
        print(title, jobSalary, work_years, education)
        all_job.append([title, jobSalary, work_years, education, jd])
        # break


def parseDetal(href):
    ret = requests.get(href, headers)
    bs_ret = BeautifulSoup(ret.text, 'lxml').find('dd', {'data-selector': 'job-intro-content'}).text
    return bs_ret


def main():
    cookies = {
        'gr_user_id': '361034c2-0e63-4beb-8dcd-13218d20934c',
        'gr_session_id_97dcf586237881ba': 'f0c3c498-8035-431e-8e6c-ee93450f3878',
        '__uuid': '1648044151456.52',
        '__tlog': '1648044151457.99%7C00000000%7C00000000%7Cs_00_pz0%7Cs_00_pz0',
        '__gc_id': 'faea224340e14348be6fb35a6573dc24',
        'UniqueKey': '3b4a09a592219b8f1a667e00ad0d9493',
        'lt_auth': '7bkNOHBUmVWq5yaMimRWsasY2tKoUj%2BdoCkKgRlTgIfvW6G04PnqSgKCp7EExAMhk0t9dcULN7T2%0D%0ANez6ynVL4kMSwGmmloC4uOW91mEJRt11HuyflMX8k87XQqUkrXg6yUpynw%3D%3D%0D%0A',
        'inited_user': '749e3310dd6f7ad8a822a5120e6e5f5f',
        'user_roles': '0',
        'user_photo': '5f8fa3a679c7cc70efbf444e08u.png',
        'user_name': '%E5%91%A8%E6%99%A8%E9%98%B3',
        'need_bind_tel': 'false',
        'new_user': 'false',
        'c_flag': '2585ea4fb8de5f1c96fb8b87132d40f5',
        '__s_bid': '500af6b70816614dcb0de2f7085a1aee8c90',
        'imClientId': '9fcfdc133ce76755b1921abcfab3aed0',
        'imId': '9fcfdc133ce767556882ca1e5431db9c',
        'imClientId_0': '9fcfdc133ce76755b1921abcfab3aed0',
        'imId_0': '9fcfdc133ce767556882ca1e5431db9c',
        'imApp_0': '1',
        'fe_se': '-1648044396728',
        'acw_tc': '2760829f16480502276646112e38dc2a84eee23979ebe91370979c9f0dccd6',
        'fe_im_connectJson_0': '%7B%220_3b4a09a592219b8f1a667e00ad0d9493%22%3A%7B%22socketConnect%22%3A%221%22%2C%22connectDomain%22%3A%22liepin.com%22%7D%7D',
        '__session_seq': '36',
        '__uv_seq': '36',
        'fe_im_socketSequence_new_0': '35_34_32',
    }
    # for x in range(0, 3):
    params = (
        ('headId', '6d7e03665a77f47c27b77b717414fe20'),
        ('ckId', 'ynh9pnc2s2db2l4g94fa4g2rzidggpg9'),
        ('oldCkId', '937235055034adc4f1981eee1dbd46d2'),
        ('fkId', 'buz8mt9nxipxj0fwytoddi68vv99sp8a'),
        ('skId', '9lql5dwaasm6v4m4kvno3hrzfhuf9ysb'),
        ('sfrom', 'search_job_pc'),
        ('key', '新媒体'),
        ('industry', '10$270'),
        ('dq', '050090'),
        ('currentPage', '2'),
        ('scene', 'page'),
    )

    response = requests.get('https://www.liepin.com/zhaopin/', headers=headers, params=params, cookies=cookies)
    # print(response.text)
    bs_ret = BeautifulSoup(response.text, 'lxml')
    parse_info(bs_ret)
    time.sleep(2)
    # print(x)


if __name__ == '__main__':
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://www.liepin.com/zhaopin/?headId=6d7e03665a77f47c27b77b717414fe20&ckId=i3pxqw5v19wmaldvkrh8ymtqc3cua4ea&oldCkId=28f412667200ed7e34524df8296ea0df&fkId=un6v1x7nanfbjhmdj3sy8v78nu9ejd29&skId=9lql5dwaasm6v4m4kvno3hrzfhuf9ysb&sfrom=search_job_pc&key=%E6%96%B0%E5%AA%92%E4%BD%93&dq=050090&currentPage=1&scene=page',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    all_job = []
    main()
    keyWord = '新媒体-猎聘2'
    processing_data(all_job)
