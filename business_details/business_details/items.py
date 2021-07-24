# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class BusinessDetailsItem(scrapy.Item):
    # define the fields for your item here like:
    business_name = scrapy.Field()
    address = scrapy.Field()
    numbers = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()