#!/usr/bin/env python
# encoding: utf-8
import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.search import SearchSpider
from spiders.search_text import SearchTextSpider

if __name__ == '__main__':
    mode = sys.argv[1]
    # mode = 'search'
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    mode_to_spider = {
        'search': SearchSpider,
        'search_text': SearchTextSpider,
    }
    process.crawl(mode_to_spider[mode])
    # the script will block here until the crawling is finished
    process.start()
