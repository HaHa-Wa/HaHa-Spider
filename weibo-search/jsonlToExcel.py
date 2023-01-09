# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/8 10:27 下午
@Auth ： HaHa-Wa
@File ：test.py
@IDE ：PyCharm
"""
import json

import pandas as pd
with open('output/search_spider_20230107115712.jsonl', 'r', encoding='utf-8')as f:
    ret = f.readlines()

json_dict = []
for i, x in enumerate(ret):
    haha = json.loads(x)
    json_dict.append(haha)
pdObj = df = pd.json_normalize(json_dict)

print(pdObj)
pdObj.to_excel('test.xlsx', encoding='utf-8')
