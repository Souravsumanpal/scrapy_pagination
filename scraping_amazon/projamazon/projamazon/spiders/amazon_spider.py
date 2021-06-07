import scrapy
from ..items import ProjamazonItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_binding_browse-bin%3A1318375031&dc&qid=1620978700&rnid=1318374031&ref=sr_nr_p_n_binding_browse-bin_4'
    ]

    def parse(self, response):
        items = ProjamazonItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-spacing-none:nth-child(1) .a-row .a-size-base:nth-child(2)').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink
        
        yield items
