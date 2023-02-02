# -*- coding: utf-8 -*-
"""
@Time ： 2023/2/1 11:58 下午
@Auth ： HaHa-Wa
@File ：read_mongodb.py
@IDE ：PyCharm
"""
import pymongo
import pandas as pd

# 连接mongodb数据库
from pymongo import MongoClient

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'meishijie'
MONGODB_CNAME = 'meishi'

client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
# 连接数据库
mydb = client[MONGODB_DBNAME]
post1 = mydb[MONGODB_CNAME]
post2 = mydb['meishi2']


def insert_mongo(item):
    data = dict(item)
    post2.insert(data)
    return item


# 将mongodb中的数据读出
ret = list(post1.find())
# print(ret)
all_info = {}
for rt in ret:
    href = rt['href']
    if href not in all_info:
        all_info[href] = rt
        all_info[href]['tag'] = [rt['name1']]
    else:
        if rt['name1'] not in all_info[href]['tag']:
            all_info[href]['tag'].append(rt['name1'])
            print(all_info[href]['tag'])
            # break

for x, y in all_info.items():
    # print(y)
    data_info = {'name1': y['name1'],
                 'name2': y['name2'],
                 'href': y['href'],
                 'tag': y['tag']}
    insert_mongo(data_info)

    # break
    # insert_mongo(x)
print(len(all_info.keys()))
