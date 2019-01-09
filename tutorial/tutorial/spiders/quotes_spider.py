import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
    'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)
