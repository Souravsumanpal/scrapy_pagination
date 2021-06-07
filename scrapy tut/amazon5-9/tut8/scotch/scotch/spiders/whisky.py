import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    allowed_domains = ['a.com']
    start_urls = ['http://a.com/']

    def parse(self, response):
        pass
