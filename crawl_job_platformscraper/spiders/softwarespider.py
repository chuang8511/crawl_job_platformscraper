import scrapy
# todo: 
# 1. get all salary to check the average salary
# 2. divide the salary by the district
# 3. divide the salary by the industry
# 4. divide the salary by the work content
# 5. divide the salary by the working experience


class SoftwarespiderSpider(scrapy.Spider):
    name = "softwarespider"
    allowed_domains = ["www.104.com.tw"]
    start_urls = ["https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=%E8%BB%9F%E9%AB%94%E5%B7%A5%E7%A8%8B%E5%B8%AB&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=12&asc=0&page=4&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"]

    def parse(self, response):
        
        pass
