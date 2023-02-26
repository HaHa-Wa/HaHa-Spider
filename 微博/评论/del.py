# -*- coding: utf-8 -*-
"""
@Time ： 2023/1/26 7:45 下午
@Auth ： HaHa-Wa
@File ：del.py
@IDE ：PyCharm
"""
import pandas as pd
import re
file_name = 'test.xlsx'

df = pd.read_excel(file_name)
all_info = []
for x in df.itertuples():
    x = list(x)
    try:
        x[5] = re.sub(r"\[\S+\]", "", x[5])
        if len(x[5]) != 0:
            all_info.append(x)
        print(x[5])

    except:
        pass
# text = '以前说人口太多了，现在也不怕跌嘛。[二哈]'
# text = re.sub(r"\[\S+\]", "", text)  # 去除表情符号
# print(text)
haha = pd.DataFrame(all_info)
haha.to_excel('ret.xlsx')
