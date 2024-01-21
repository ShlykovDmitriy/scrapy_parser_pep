import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):
    """Паук для парсинга информации с сайта peps.python.org."""
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Парсинг ссылок на страницы PEP"""
        all_pep = response.xpath('//*[@id="numerical-index"]')
        for pep in all_pep.css("a::attr(href)").getall():
            yield response.follow(pep, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Парсинг информации со страниц PEP:
        - номер
        - название
        - статус
        """
        h1_tag = response.css('h1.page-title::text').get()
        data = {
            'number': h1_tag.split(' – ')[0][4:],
            'name': h1_tag.split(' – ')[1],
            'status': response.css("dt:contains('Status') + dd ::text").get(),
        }
        yield PepParseItem(data)
