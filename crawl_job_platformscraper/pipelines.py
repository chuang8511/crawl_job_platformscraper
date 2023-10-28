# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class CrawlJobPlatformscraperPipeline:
    def process_item(self, item, spider):
        return item


class SavingToPostgresPipeline(object):

    def process_item(self, item, spider):
        conn = psycopg2.connect(
                    host="localhost",
                    database="jobs_test",
                    user="c.huang")
        
        data = (item['title'], item['industry'], item['location'])
        query  = "INSERT INTO jobs (title, industry, location) VALUES (%s, %s, %s)"
        cur = conn.cursor()
        cur.execute(query, data)
        conn.commit()

        cur.close()
        conn.close()

        #we need to return the item below as scrapy expects us to!
        return item