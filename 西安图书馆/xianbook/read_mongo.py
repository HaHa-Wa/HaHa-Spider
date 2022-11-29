# import xlwt
import pymongo
import pandas as pd

# 连接mongodb数据库
client = pymongo.MongoClient("localhost")
# 连接数据库
db = client["data"]
# 数据表
douban = db["xianbook"]
# 将mongodb中的数据读出
data = pd.DataFrame(list(douban.find()))

# 保存为csv格式
data.to_csv('data.csv', encoding='utf-8')
# 保存为xls格式
# data.to_excel('data.xls', encoding='utf-8')
