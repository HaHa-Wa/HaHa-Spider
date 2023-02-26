# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/19 11:15 下午
@Auth ： HaHa-Wa
@File ：new_main.py
@IDE ：PyCharm
"""
import os
import re
import json
import asyncio
import time
import aiohttp
import execjs
import pandas as pd
from bs4 import BeautifulSoup


class EmailDeleter(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }

    def __init__(self, username, password):
        self.client = None
        self.username = username
        self.password = password
        self.sid = None
        self.all_info = []

    async def extract_login_form(self):
        """提取登录表单"""
        url = 'https://exmail.qq.com/cgi-bin/loginpage'
        async with self.client.get(url, verify_ssl=False) as r:
            resp = await r.text()
        doc = BeautifulSoup(resp, 'lxml')

        fingerprint_deviceid = doc.find('input', {'name': "fingerprint_deviceid"})['value']
        ts = doc.find('input', {'name': "ts"})['value']
        content = f'{self.password}\n{ts}\n'
        with open('jm.js', 'r') as f:
            js = execjs.compile(f.read())
            p = js.call('Q', content)  # 执行处理好的js文件,返回加密串
        data = {
            'fingerprint_deviceid': fingerprint_deviceid,
            'device_type': 'web',
            'device_name': 'chrome',
            'sid': '',
            'firstlogin': 'false',
            'domain': self.username.split('@')[1],
            'aliastype': 'other',
            'errtemplate': 'dm_loginpage',
            'first_step': '',
            'buy_amount': '',
            'year': '',
            'company_name': '',
            'is_get_dp_coupon': '',
            'source': '',
            'qy_code': '',
            'origin': '',
            'starttime': time.time(),
            'redirecturl': '',
            'redirect_hash': '',
            'f': 'biz',
            'uin': self.username.split('@')[0],
            'p': p,
            'login_from': '',
            'vt': '',
            'delegate_url': '',
            'ts': ts,
            'from': '',
            'ppp': '',
            'chg': '0',
            'domain_bak': '0',
            'no_force_scan': '0',
            'loginentry': '3',
            's': '',
            'dmtype': '',
            'fun': '',
            'area': '',
            'mobile': '',
            'phone_vc': '',
            'inputuin': self.username,
            'pp': self.password,
            'verifycode': '',
            'data-statistic-login-type': 'home_login',
        }

        return data

    async def login(self):
        """登录企业邮箱"""
        url = 'https://exmail.qq.com/cgi-bin/login'
        data = await self.extract_login_form()

        async with self.client.post(
                url,
                data=data,
                headers=self.headers,
                verify_ssl=False
        ) as r:
            resp = await r.text()

        return resp

    async def get_folder_info(self, resp):
        """获取首页"""
        self.sid = sid = re.findall(r'"frame_html\?sid=(.*?)"', resp)[0]
        r = re.findall(r'targetUrl\+="\&r=(.*?)";', resp)[0]
        url = f'https://exmail.qq.com/cgi-bin/frame_html?sid={sid}&r={r}'
        async with self.client.get(
                url,
                headers=self.headers,
                verify_ssl=False
        ) as r:
            resp = await r.text()
        if self.username in resp:  # 校验是否登录成功
            print('登录成功')
        else:
            print('登录失败')
            exit()
        f = re.findall(r'originUserFolders = (.*?);', resp.replace('\n', ''))[1]
        f = f.replace('id', '"id"')  # 替换成json可处理的格式
        f = f.replace('name', '"name"')
        f = f.replace('father"id"', '"fatherid"')
        f = f.replace('unread', '"unread"')
        f = f.replace('children', '"children"')
        f = f.replace('level', '"level"')
        f = f.replace('isLeaf', '"isLeaf"')
        folder_info = json.loads(f)
        for i in folder_info:
            print(f'name:{i["name"]} id:{i["id"]}')

    async def time_date(self):
        time_local = time.localtime(time.time())
        # 转换成新的时间格式(精确到秒)
        dt = time.strftime("%Y-%m-%d %H-%M", time_local)
        return dt

    async def get_list(self, page_):
        for page in range(0, int(page_)):
            print('page:', page)
            url = 'https://exmail.qq.com/cgi-bin/mail_list?sid=vVdEU_P5usoy1wlq,7&page={0}&folderid=1&flag=&fun=&s=inbox&searchmode=&filetype=&listmode=&stype=&ftype=&AddrID=&showattachtag='.format(
                page)
            async with self.client.get(
                    url,
                    headers=self.headers,
            )as r:
                response = await r.text()
            ret = BeautifulSoup(response, 'lxml')
            toareas = ret.find_all('div', class_='toarea')
            for toarea in toareas:
                tables = toarea.find_all('table', class_='i M')
                for table in tables:
                    # print(table)
                    mail_id = table.find('input', {'name': 'mailid'})['value']
                    send_name = table.find('td', class_='tl tf').text
                    zhuti = table.find('td', class_='gt tf').find('u', class_='black').text
                    send_time = table.find('td', class_='dt').text

                    print(send_name, zhuti, send_time, '\n')
                    content, data_time, receice_name = await self.get_detail(zhuti, mail_id)
                    self.all_info.append([send_name, receice_name, zhuti, data_time, content])
        df = pd.DataFrame(self.all_info)
        da_time = await self.time_date()
        xlsx_name = '邮件数据' + da_time + '.xlsx'
        # with pd.ExcelWriter(xlsx_name, engine='xlsxwriter', options={'strings_to_urls': False}) as writer:
        df.to_excel(xlsx_name, index=False)

    async def get_detail(self, zhuti, mail_id):
        # mail_id = 'ZL3507-mHLt2WksnOwN3wFiPrNeNde'
        url = f'https://exmail.qq.com/cgi-bin/readmail?folderid=1&t=readmail&mailid={mail_id}&mode=pre&maxage=3600&base=10.7710&ver=12291&sid=vVdEU_P5usoy1wlq,7&show_ww_icon=false'
        async with self.client.get(url, headers=self.headers, ) as r:
            resp = await r.text()

        ret = BeautifulSoup(resp, 'lxml')
        contentDiv = ret.find('div', id='contentDiv')
        content = contentDiv.text
        data_time = ret.find('div', class_='receiver-inline-wrap').find('div', class_='cont tcolor').text
        try:
            receice_name = ret.find('span', class_='receiver-item-span').text
        except:
            receice_name = ''
        file_list = []
        name_bigs = ret.find_all('div', class_='name_big')
        for name_big in name_bigs:
            href = 'https://exmail.qq.com' + name_big.find('a')['href']

            file_name = name_big.find('span').text
            print(file_name, href)
            file_list.append([file_name, href])
            await self.dowlound(zhuti, file_name, href)
        return content, data_time, receice_name

    async def dowlound(self, zhuti, file_name, url):

        async with self.client.get(
                url,
                headers=self.headers,
        ) as r:
            resp = await r.content.read()
        main_path = 'file/' + zhuti[:30].replace(':', '').replace('*', '') \
            .replace('/', '').replace('|', '').replace('\\', '').replace('<', '').replace('>', '')
        if not os.path.exists(main_path):
            os.mkdir(main_path)
        file_path = main_path + '/' + file_name
        try:
            with open(file_path, 'wb') as f:
                f.write(resp)
        except:
            pass

    async def run(self):
        self.client = aiohttp.ClientSession()
        resp = await self.login()
        await self.get_folder_info(resp)

        page_ = input('输入采集页码:')
        await self.get_list(page_)
        await asyncio.sleep(2)
        await self.client.close()


if __name__ == '__main__':
    # email = input('输入邮箱：')
    # password = input('输入密码：')
    email = '账号'
    password = '密码'
    e = EmailDeleter(email, password)
    asyncio.run(e.run())
