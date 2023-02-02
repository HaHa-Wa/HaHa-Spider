# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter

from meishijie.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME, MONGODB_CNAME


class MeishijiePipeline:
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        cname = MONGODB_CNAME
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[cname]

    # 将数据存入mongodb
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
