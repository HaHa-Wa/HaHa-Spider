import datetime
import json
import time
import requests
import scrapy
from scrapy.http import JsonRequest
from fake_useragent import UserAgent

from juchao.items import FileItem

ua = UserAgent()


class ReportSpider(scrapy.Spider):
    name = 'report'
    allowed_domains = ['cninfo.com.cn']
    start_urls = ['http://cninfo.com.cn/']

    def start_requests(self):
        start_time = '2022-09-16'
        end_time = '2023-01-14'
        csv_file_name = start_time + ' ' + end_time + '.xlsx'
        d_pdf = False
        # sec_code_list = ['000010,gssz0000010', '000796,gssz0000796', '000797,gssz0000797', '000798,gssz0000798',
        #                  '000799,gssz0000799']
        sec_code_list = []
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')
        time_spread = datetime.timedelta(days=1)
        if sec_code_list:
            for code in sec_code_list:
                while start_time <= end_time:
                    s_time = start_time.strftime("%Y-%m-%d")
                    e_time = (start_time + time_spread + time_spread + time_spread).strftime("%Y-%m-%d")
                    body = {
                        "pageNum": '1',
                        "pageSize": '30',
                        'column': 'szse',
                        'tabName': "fulltext",
                        'plate': "",
                        'stock': code,
                        'searchkey': "",
                        'secid': "",
                        'category': "",
                        'trade': "",
                        'seDate': "{0}~{1}".format(s_time, e_time),
                        'sortName': "",
                        'sortType': "",
                        'isHLtitle': "true"
                    }
                    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
                    max_page = get_max_page(body)
                    for page in range(1, max_page + 1):
                        body['pageNum'] = str(page)
                        yield scrapy.FormRequest(url, formdata=body, callback=self.parse,
                                                 meta={'d_pdf': d_pdf, 'csv_name': csv_file_name})

                    start_time = start_time + time_spread + time_spread + time_spread + time_spread
        else:
            while start_time <= end_time:
                s_time = start_time.strftime("%Y-%m-%d")
                e_time = (start_time + time_spread).strftime("%Y-%m-%d")
                body = {
                    "pageNum": '1',
                    "pageSize": '30',
                    'column': 'szse',
                    'tabName': "fulltext",
                    'plate': "",
                    'stock': "300085,9900012331",
                    'searchkey': "",
                    'secid': "",
                    'category': "",
                    'trade': "",
                    'seDate': "{0}~{1}".format(s_time, e_time),
                    'sortName': "",
                    'sortType': "",
                    'isHLtitle': "true"
                }
                url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
                max_page = get_max_page(body)
                for page in range(1, max_page + 1):
                    body['pageNum'] = str(page)
                    yield scrapy.FormRequest(url, formdata=body, callback=self.parse,
                                             meta={'d_pdf': d_pdf, 'csv_name': csv_file_name})

                start_time = start_time + time_spread + time_spread

    def parse(self, response, *args, **kwargs):
        d_pdf = response.meta['d_pdf']
        csv_file_name = response.meta['csv_name']
        json_res = json.loads(response.text)
        announcements = json_res['announcements']
        if announcements:
            for announcement in announcements:
                secCode = announcement['secCode']
                secName = announcement['secName']
                announcementTitle = announcement['announcementTitle']
                announcementTime = announcement['announcementTime']
                announcementTime = time.localtime(announcementTime / 1000)
                announcementTime = time.strftime("%Y-%m-%d", announcementTime)
                announcementType = str(announcement['announcementType'].split('||'))
                announcementId = announcement['announcementId']
                pageColumn = announcement['pageColumn']
                adjunctUrl = announcement['adjunctUrl']
                adjunctUrl = 'http://static.cninfo.com.cn/' + adjunctUrl
                one_info = {
                    'secCode': secCode,
                    'secName': secName,
                    'pageColumn': pageColumn,
                    'announcementTitle': announcementTitle,
                    'announcementTime': announcementTime,
                    'announcementId': announcementId,
                    'adjunctUrl': adjunctUrl,
                    'announcementType': announcementType,
                    'csv_file_name': csv_file_name
                }
                if d_pdf:
                    file_name = adjunctUrl.split('/')[-1]
                    one_info['file_name'] = file_name
                    file_item = FileItem(file_urls=[adjunctUrl], file_name=file_name)
                    yield file_item

                yield one_info


def get_max_page(data):
    url = 'http://www.cninfo.com.cn/new/hisAnnouncement/query'
    headers = {
        "User-Agent": ua.chrome
    }
    res = requests.post(url, headers=headers, data=data)
    # try:
    json_res = json.loads(res.content.decode())
    # try:
    totalpages = json_res['totalpages']
    # except:
    #     totalpages = 1

    return totalpages
