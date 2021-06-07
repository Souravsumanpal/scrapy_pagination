# from _typeshed import FileDescriptorLike
import scrapy


class ArchinectSpiderSpider(scrapy.Spider):
    name = 'archinect_spider'
    # allowed_domains = ['archinect.com']
    start_urls = [
        'https://archinect.com/firms'
        ]

    def parse(self, response):
        for link in response.css('li a.ThumbA::attr(href)'):
            yield response.follow(link.extract(), callback=self.parse_categories)

    def parse_categories(self,response):
        descriptions = response.css('ul.CoverList')
        for description in descriptions:
            yield {
                'firm_bio' : description.css('#ProfileDescription p::text').extract(),
                'services_offered' : description.css('.TagLinks:nth-child(16) .TagLink::text').extract(),
                'markets' : description.css('.TagLinks:nth-child(20) .TagLink::text').extract(),
                'address': description.css('h2+ p::text').extract(),
                'phone' : description.css('.Phone+ .FixedWidth::text').extract(),
                'email' : description.css('.Email+ .FixedWidth a::text').extract()
            }

        next_page = response.css('.next a::attr(href)').extract()

        if next_page:
            yield response.follow(next_page[0], callback = self.parse)       

              

