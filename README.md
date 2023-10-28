# crawl_job_platformscraper
Please read the manual if you want to learn scrapy
https://www.notion.so/scrapy-892c29fad47b4b4f84ce2bb891fc6dd8
https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide/

How to export data as json or csv?
$ scrapy crawl jobplatformspider -O jobs.csv
$ scrapy crawl jobplatformspider -O jobs.json

If the data is messy, how to deal with that?
- Please try to use the item loader to pre-process the data to make the code cleaner
Doc: https://scrapeops.io/python-scrapy-playbook/scrapy-beginners-guide-cleaning-data/#example-item-loader