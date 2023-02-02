# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeishijieItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    tag = scrapy.Field()
    recipe_topimg = scrapy.Field()
    recipe_topvideo = scrapy.Field()
    gongyi = scrapy.Field()
    kouwei = scrapy.Field()
    shijian = scrapy.Field()
    nandu = scrapy.Field()
    fanliang = scrapy.Field()
    gaoxiezhi = scrapy.Field()
    jianfei = scrapy.Field()
    gaoxieya = scrapy.Field()
    gaoxietang = scrapy.Field()
    ertong = scrapy.Field()
    tang = scrapy.Field()
    reliang = scrapy.Field()
    zhifang = scrapy.Field()
    zhuliao = scrapy.Field()
    fuliao = scrapy.Field()
    recipe_step_box = scrapy.Field()
    step_box = scrapy.Field()
