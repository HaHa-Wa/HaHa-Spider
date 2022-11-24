# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class XianbookItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BookItem(Item):
    bookName = Field()
    loansNum = Field()
    zhuzhe = Field()
    press = Field()
    pressDate = Field()
    leixing = Field()
    shuhao = Field()
    timing = Field()
    isbn = Field()
    yuzhong = Field()
    xingtai = Field()
    faxing = Field()
    zhaiyao = Field()
