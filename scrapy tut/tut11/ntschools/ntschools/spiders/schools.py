import scrapy
from scrapy.http import request
import json


class SchoolsSpider(scrapy.Spider):
    name = 'schools'
    # allowed_domains = ['s']
    start_urls = ['https://directory.ntschools.net/#/schools']
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://directory.ntschools.net/',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
        'X-Requested-With': 'Fetch'
    }

    def parse(self, response):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools'
        yield scrapy.Request(url, callback=self.parse_api, headers=self.headers)

    def parse_api(self,response):
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        raw = response.body
        data = json.loads(raw)
        for school in data:
            school_code = school['itSchoolCode']
            school_url = 


