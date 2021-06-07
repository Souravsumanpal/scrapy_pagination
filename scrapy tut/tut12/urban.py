import scrapy
from scrapy.crawler import CrawlerProcess
import requests
import json


class Urban(scrapy.Spider):
    name = 'urban'

    url = 'https://www.urbandictionary.com/popular.php?character=A'

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self,res):
        # Extract data
        links = []

        for item in res.css('ul.no-bullet').css('li'):

            word = item.css('a::text').get()
            short_description = requests.get('https://api.urbandictionary.com/v0/tooltip?term=' + word +'&key=ab71d33b15d36506acf1e379b0ed07ee').json()['string'].replace('\n','').replace('\r','').replace('<b>','').replace('</b>','')

            items = {
                'word': word,
                'short_description': short_description,
                'link': item.css('a::attr(href)').get()
            }

            print(json.dumps(items, indent=2))

            break

        # follow links recursively
        for link in links['link']:
            yield res.follow(url=link, meta={'short_description': link['short_description']})

# main driver
if __name__ == '__main__':
    # run scraper
    process = CrawlerProcess()
    process.crawl(Urban)
    process.start()            