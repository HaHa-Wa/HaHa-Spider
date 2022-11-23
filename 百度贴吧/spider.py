# 导入库
import urllib.request
import json
import pymongo


# 创建数据库类 连接本地数据库
class Mongo:

    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)  # 创建链接
        # 连接所需数据库名
        db = client['baiduSpider']
        # 连接对应的库表
        self.post = db['tieba']

    # 插入一条数据
    def insert_one(self, item):
        postItem = dict(item)  # 转化为字典形式
        self.post.insert_one(postItem)  # 向表中插入一条数据
        return item  # 可以输出到控制台,可以不写

    # 插入多条数据
    def insert_many(self, item_list):
        self.post.insert_many(item_list)  # 向表中插入多条数据
        return item_list  # 可以输出到控制台,可以不写


# 采集函数
def spider(mongo_client):
    # 采集
    for page in range(1, 100):
        print('page:', page)
        url = "https://tieba.baidu.com/mg/f/getFrsData?kw=%E4%B8%AD%E5%8C%97%E5%A4%A7%E5%AD%A6&rn=10&pn={0}&is_good=0&cid=0&sort_type=0&fr=&default_pro=1&only_thread_list=0&eqid=&refer=tieba.baidu.com".format(
            page)
        ret = urllib.request.urlopen(url).read()  # 读网页
        data = json.loads(ret)['data']
        mongo_client.insert_many(data['thread_list'])
    print("***爬取数据结束***")


def main():
    # 建立数据库连接
    mongo_client = Mongo()
    # 启动爬虫代码
    spider(mongo_client)


if __name__ == '__main__':
    main()
