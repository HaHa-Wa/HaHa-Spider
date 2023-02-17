# -*- coding: utf-8 -*-
import datetime
import json
import os.path
import time

import pymongo

from settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME


class JsonWriterPipeline(object):
    """
    写入json文件的pipline
    """

    # 建立mongodb连接
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post_text = mydb['text']
        self.post_search = mydb['search']

    # 将数据存入mongodb
    def process_item(self, item, spider):
        data = dict(item)

        if spider.name == 'search_text_spider':
            self.post_text.insert(data)
        elif spider.name == 'search_spider':
            self.post_search.insert(data)
        return item


