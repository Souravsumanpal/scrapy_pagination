import scrapy
from ..items import Proj1Item

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response):

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

        # next_page = 'https://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number) +'/'
        next_page = response.css('.next a::attr(href)').extract()

        if next_page:
            yield response.follow(next_page[0],callback = self.parse)

        # if QuoteSpider.page_number <= 10:
        #     QuoteSpider.page_number += 1 
        #     yield response.follow(next_page, callback=self.parse)  
            

