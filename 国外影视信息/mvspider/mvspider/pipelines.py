# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class MvspiderPipeline:
    # 建立mongodb连接
    def __init__(self):
        host = '127.0.0.1'
        port = 27017
        self.client = pymongo.MongoClient(host=host, port=port)
        mydb = self.client['myflixer']
        self.post = mydb['tv']

    # 将数据存入mongodb
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
