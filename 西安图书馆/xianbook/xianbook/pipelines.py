import pymongo
from xianbook.settings import MONGODB_HOST, MONGODB_PORT, MONGODB_CNAME, MONGODB_DBNAME


class XianbookPipeline:
    def __init__(self):
        host = MONGODB_HOST
        port = MONGODB_PORT
        dbname = MONGODB_DBNAME
        cname = MONGODB_CNAME
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[cname]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
