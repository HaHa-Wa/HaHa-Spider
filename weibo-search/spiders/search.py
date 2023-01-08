#!/usr/bin/env python
# encoding: utf-8
import datetime
import json
import re
from scrapy import Spider, Request
from spiders.common import parse_tweet_info, parse_long_tweet


class SearchSpider(Spider):
    """
    关键词搜索采集
    """
    name = "search_spider"
    base_url = "https://s.weibo.com/"

    def start_requests(self):
        """
        爬虫入口
        """
        # 这里keywords可替换成实际待采集的数据
        start_time = datetime.datetime.strptime("2021-01-01", '%Y-%m-%d')
        end_time = datetime.datetime.strptime("2021-01-02", '%Y-%m-%d')
        time_spread = datetime.timedelta(days=1)
        keyword = '新冠'
        urls = []
        while start_time <= end_time:
            day_string = start_time.strftime("%Y-%m-%d")
            for hour in range(1, 24):
                start_string = day_string + '-' + str(hour - 1)
                end_string = day_string + '-' + str(hour)
                url = f"https://s.weibo.com/weibo?q={keyword}&timescope=custom%3A{start_string}%3A{end_string}&page=1"
                print(url)
                urls.append(url)
            start_time = start_time + time_spread
        for url in urls:
            yield Request(url, callback=self.parse, meta={'keyword': keyword})

    def parse(self, response, **kwargs):
        """
        网页解析
        """
        html = response.text
        tweet_ids = re.findall(r'\d+/(.*?)\?refer_flag=1001030103_" ', html)
        for tweet_id in tweet_ids:
            url = f"https://weibo.com/ajax/statuses/show?id={tweet_id}"
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
