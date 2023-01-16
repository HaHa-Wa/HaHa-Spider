# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InterItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    detail_url = scrapy.Field()
    titre = scrapy.Field()
    Dep = scrapy.Field()
    Ville = scrapy.Field()
    Derniere_session = scrapy.Field()
    Organisme = scrapy.Field()
    Publics = scrapy.Field()
    collapseCertifs = scrapy.Field()
    collapseObjectifs = scrapy.Field()
    collapseMetiers = scrapy.Field()
    collapseDuree = scrapy.Field()
    collapseConditionAcces = scrapy.Field()
    collapseLieuReal = scrapy.Field()
    collapsePeriode = scrapy.Field()
    collapseOresp = scrapy.Field()
