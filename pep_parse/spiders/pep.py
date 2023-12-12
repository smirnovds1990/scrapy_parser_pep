import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        links = response.css('a.pep reference internal::attr(href)')
        print(links)
    #     for link in links:
    #         yield response.follow(link, callback=self.parse_pep)

    # def parse_pep(self, response):
    #     data = {
    #         'number': response.css('h1::text').get().split('–')[0].strip(),
    #         'name': response.css('h1::text').get().split('–')[1].strip(),
    #         'status': response.css('dt:contains("Status") + dd::text').get()
    #     }
    #     yield PepParseItem(data)
