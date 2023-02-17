#!/usr/bin/env python
# encoding: utf-8
import datetime
import json
import re

from pymongo import MongoClient
from scrapy import Spider, Request
from spiders.common import parse_tweet_info, parse_long_tweet


class SearchSpider(Spider):
    """
    关键词搜索采集
    """
    name = "search_spider"
    base_url = "https://s.weibo.com/"
    wb_id = []
    def start_requests(self):
        """
        爬虫入口
        """
        self.wb_id = read_mongo()
        # 这里keywords可替换成实际待采集的数据
        start_time = datetime.datetime.strptime("2022-12-01", '%Y-%m-%d')
        end_time = datetime.datetime.strptime("2023-01-31", '%Y-%m-%d')
        time_spread = datetime.timedelta(days=1)
        keyword = ['阳过', '阳康', '阳了', '新冠', '疫情']
        urls = []
        while start_time <= end_time:
            for key in keyword:
                day_string = start_time.strftime("%Y-%m-%d")
                for hour in range(17, 24):
                    start_string = day_string + '-' + str(hour - 1)
                    end_string = day_string + '-' + str(hour)
                    # start_string = day_string + '-' + str(17)
                    # end_string = day_string + '-' + str(24)
                    url = f"https://s.weibo.com/weibo?q={key}&timescope=custom%3A{start_string}%3A{end_string}&page=1"
                    print(url)
                    urls.append([url, key])
            start_time = start_time + time_spread
        for url in urls:
            yield Request(url[0], callback=self.parse, meta={'keyword': url[1]})

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        html = response.text
        tweet_ids = re.findall(r'weibo.com/\d+/(.*?)\?refer_flag=1001030103_" ', html)
        for tweet_id in tweet_ids:
            if tweet_id not in self.wb_id:
                url = f"https://weibo.com/ajax/statuses/show?id={tweet_id}"
                self.wb_id.append(tweet_id)
                yield Request(url, callback=self.parse_tweet, meta=response.meta)
        next_page = re.search('<a href="(.*?)" class="next">下一页</a>', html)
        if next_page:
            url = "https://s.weibo.com" + next_page.group(1)
            yield Request(url, callback=self.parse, meta=response.meta)

    @staticmethod
    def parse_tweet(response):
        """
        解析推文
        """
        data = json.loads(response.text)
        item = parse_tweet_info(data)
        item['keyword'] = response.meta['keyword']
        if item['isLongText']:
            url = "https://weibo.com/ajax/statuses/longtext?id=" + item['mblogid']
            yield Request(url, callback=parse_long_tweet, meta={'item': item})
        else:
            yield item

def read_mongo():
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
    MONGODB_DBNAME = 'weibo'
    MONGODB_CNAME = 'search'

    client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT)
    # 连接数据库
    mydb = client[MONGODB_DBNAME]
    post1 = mydb[MONGODB_CNAME]
    ret = post1.find()
    web_id = [x['mblogid'] for x in ret]
    return web_id
