# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlJobPlatformscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass

class Job(scrapy.Item):
    title = scrapy.Field()
    industry = scrapy.Field()
    location = scrapy.Field()