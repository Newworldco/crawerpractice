import scrapy

class DmozSpider(scrapy.Spider):
    name = 'jandan'
    allowed_domain = ['jandan.net']
    start_urls = ['http://jandan.net/ooxx/page-30#comments']

    def parse(self, response):
        sel = scrapy.selector.Selector(response)

        sites = sel.xpath()