import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://' + domain + '/' for domain in allowed_domains]

    def parse(self, response):
        links = response.css('a.pep::attr(href)')
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text').get()
        page_title = page_title.split(' – ')
        data = {
            'number': page_title[0],
            'name': page_title[1],
            'status': response.css('dt:contains("Status") + dd abbr::text')
            .get()
        }
        yield PepParseItem(data)
