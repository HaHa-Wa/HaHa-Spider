# -*- coding: utf-8 -*-
import datetime
import json
import os.path
import time

import pymongo

from settings import MONGODB_HOST, MONGODB_PORT, MONGODB_DBNAME, MONGODB_CNAME


class JsonWriterPipeline(object):
    """
    写入json文件的pipline
    """

    # def __init__(self):
    #     self.file = None
    #     if not os.path.exists('output'):
    #         os.mkdir('output')
    #
    # def process_item(self, item, spider):
    #     """
    #     处理item
    #     """
    #     if not self.file:
    #         now = datetime.datetime.now()
    #         file_name = spider.name + "_" + now.strftime("%Y%m%d%H%M%S") + '.jsonl'
    #         self.file = open(f'output/{file_name}', 'wt', encoding='utf-8')
    #     item['crawl_time'] = int(time.time())
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     # self.file.flush()
    #     return item
# 建立mongodb连接
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
