import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    starts_urls = ['https://www.whiskyshop.com/ws/sitemap.xml']


    def parse(self, response):
        for products in response.css('div.product-item-info'):
            yield {
                'name': products.css('a.product-item-link::text').get(),
                'price': products.css('span.price::text').get().replace('£',''),
                'link': products.css('a.product-item-link').attrib['href'],
            }