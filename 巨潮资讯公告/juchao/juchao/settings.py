# Scrapy settings for juchao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'juchao'

SPIDER_MODULES = ['juchao.spiders']
NEWSPIDER_MODULE = 'juchao.spiders'
ITEM_PIPELINES = {
    'juchao.pipelines.JuchaoPipeline': 300,
    'juchao.pipelines.MyFilesPipeline': 1
}
FILES_STORE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pdf_file')
LOG_LEVEL = 'DEBUG'
COOKIES_ENABLED = False
CONCURRENT_REQUESTS = 5  # 并发量

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'juchao (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32
