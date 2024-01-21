import scrapy


class PepParseItem(scrapy.Item):
    """Класс Item для парсинга PEP"""
    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
