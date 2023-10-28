import scrapy
import pdb
from crawl_job_platformscraper.items import Job

class JobplatformspiderSpider(scrapy.Spider):
    name = "jobplatformspider"
    allowed_domains = ["talent.104.com.tw"]
    start_urls = ["https://talent.104.com.tw/joblist"]

    def parse(self, response):
        jobTitles = response.css('.jobList_jobName_job::text').getall()
        jobIndustries = response.css('.jobList_jobName_address span:first-child::text').getall()
        jobAddresses = response.css('.jobList_jobName_address span:nth-child(2)::text').getall()

        # jobs = []
        job = Job()
        for i in range(len(jobTitles)):
            # jobs.append({
            #     'title': jobTitles[i],
            #     'industry': jobIndustries[i],
            #     'location': jobAddresses[i]
            # })
            job["title"] = jobTitles[i]
            job["industry"] = jobIndustries[i]
            job["location"] = jobAddresses[i]
            yield job
          
        # pdb.set_trace()
        
