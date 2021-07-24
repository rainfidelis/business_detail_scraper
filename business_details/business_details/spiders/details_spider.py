import scrapy
from ..items import BusinessDetailsItem


class FLSpider(scrapy.Spider):

    name = 'detail_bot'
    start_urls = [
        'https://www.finelib.com/'
    ]

    def parse(self, response):
        city_links = response.css('.city-list a::attr(href)').extract()
        for link in city_links:
            yield response.follow(link, callback=self.city_parse)

    def city_parse(self, response):
        # city = response.css('.box-new-hed::text').extract_first()
        category_links = response.css('.city-list-col a::attr(href)').extract()
        for link in category_links:
            yield response.follow(link, callback=self.category_parse)

    def category_parse(self, response):
        business_links = response.css('.box-new-hed a::attr(href)').extract()
        for link in business_links:
            yield response.follow(link, callback=self.business_parse)

        next_page = response.css('.active~ a+ a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.category_parse)

    def business_parse(self, response):
        items = BusinessDetailsItem()

        business_name = response.css('title::text').extract_first().split('-')[0].strip()
        address = response.css('.inline > .cmpny-lstng-1::text').extract_first().strip()
        numbers = response.css('.tel-no-div > .cmpny-lstng-1 a::text').extract()
        email = response.css('p > a::text').extract_first()
        website = response.css('.url a::attr(href)').extract_first()

        items['business_name'] = business_name
        items['address'] = address
        items['numbers'] = numbers
        items['email'] = email
        items['website'] = website

        yield items