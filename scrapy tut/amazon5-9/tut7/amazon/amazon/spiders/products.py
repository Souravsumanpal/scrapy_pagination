import scrapy



class ProductsSpider(scrapy.Spider):
    name = 'products'
    # allowed_domains = ['amazon.com']
    # start_urls = ['https://www.amazon.in/s?k={search}']

    def __init__(self, search='', **kwargs):
        self.start_urls = [f'https://www.amazon.in/s?k={search}']  
        super().__init__(**kwargs)  
    

    def parse(self, response):
        next_page = 0
        # items = AmazonItem()
        for products in response.css('div.sg-col-inner'):
            yield {
                'title' : products.css('.a-size-medium').css('::text').extract(),
                'views' : products.css('.a-size-small .a-size-base').css('::text').extract(),
                'price' : products.css('.a-price-whole').css('::text').extract()
            }


        next_page = response.css(".a-last a::attr(href)").extract()

        if next_page:
            yield response.follow(next_page[0], callback=self.parse)























        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)














            # title = response.css('.a-size-medium').css('::text').extract()
            # price = response.css('.a-price-whole').css('::text').extract()
            # views = response.css('.a-size-small .a-size-base').css('::text').extract()

            # items['title'] = title
            # items['price'] = price
            # items['views'] = views

            # yield items



    #     for link in response.css('.a-link-normal a-text-normal::attr(href)'):
    #         yield response.follow(link.extract, callback=self.parse_categories)


    # def parse_categories(self,response):
    #     descriptions = response.css('div#centerCol') 
    #     for description in descriptions:
    #         yield {
    #             'title' : description.css('#productTitle::text').extract(),
    #             'price' : description.css('#priceblock_ourprice::text').extract()
    #         }
