# -*- coding: utf-8 -*-
import scrapy


class CoronavirusSpider(scrapy.Spider):
    name = 'coronavirus'
    # allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/coronavirus']

    def parse(self, response):
        link = response.css('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[2]/a').get()
        name = response.css('//*[@id="main_table_countries_today"]/tbody[1]/tr[5]/td[2]/a').get()

        yield {
            'country_name': name,
            'country_link' : link
        }

