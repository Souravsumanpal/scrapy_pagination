import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import Proj1Item


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username' : 'sourav@gmail.com',
            'password' : '12345'
        }, callback=self.start_scrapy)

    def start_scrapy(self,response):
        open_in_browser(response)
        items = Proj1Item()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            
            yield items 