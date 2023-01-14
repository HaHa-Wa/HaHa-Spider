# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from openpyxl import Workbook
from scrapy.pipelines.files import FilesPipeline
import pandas as pd

class JuchaoPipeline:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        TITLE = ['代码', '简称', '板块', '公告标题', '公告时间', '公告ID', 'PDF链接', '公告类型', '文件名']
        self.all_info = [TITLE]
        # self.ws.append(TITLE)
        self.file_name = "test.xlsx"


    def process_item(self, item, spider):
        if not item.get('secCode'):
            return item
        line = [item['secCode'], item['secName'], item['pageColumn'], item['announcementTitle'],
                item['announcementTime'], item['announcementId'], item['adjunctUrl'], item['announcementType'], item.get('file_name')]
        self.all_info.append(line)
        self.file_name = item['csv_file_name']

        # self.ws.append(line)
        # self.wb.save(item['csv_file_name'])
        return item

    def close_spider(self, spider):
        # 关闭
        # self.wb.close()
        df = pd.DataFrame(self.all_info)
        df.to_excel(self.file_name)


class MyFilesPipeline(FilesPipeline):
    def file_path(self, request, item=None, response=None, info=None):
        file_name = item['file_name']
        # path = urlparse(request.url).path
        return file_name
