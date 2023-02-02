# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/30 10:04 下午
@Auth ： HaHa-Wa
@File ：test.py
@IDE ：PyCharm
"""
import pandas as pd
from pymongo import MongoClient


MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = '51job'
MONGODB_CNAME = 'post'
client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
mydb = client[MONGODB_DBNAME]
post = mydb[MONGODB_CNAME]

ret = pd.DataFrame(list(post.find()))
ret.to_csv('job.csv')
client.close()
