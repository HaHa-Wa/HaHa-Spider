# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class InterPipeline:
    def __init__(self):
        # TITLE = ['代码', '简称', '板块', '公告标题', '公告时间', '公告ID', 'PDF链接', '公告类型', '文件名']
        self.all_info = []
        # self.ws.append(TITLE)
        self.file_name = "test.xlsx"

    def process_item(self, item, spider):
        # if not item.get('secCode'):
        #     return item
        line = [x for x in item.values()]
        self.all_info.append(line)
        # self.file_name = item['csv_file_name']

        # self.ws.append(line)
        # self.wb.save(item['csv_file_name'])
        return item

    def close_spider(self, spider):
        # 关闭
        # self.wb.close()
        df = pd.DataFrame(self.all_info)
        df.to_excel(self.file_name)
