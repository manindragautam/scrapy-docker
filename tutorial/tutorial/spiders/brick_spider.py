import scrapy


class BrickSpider(scrapy.Spider):
    name = "brick"

    start_urls = [
    'https://www.brickworkratings.com/CreditRatings.aspx',
    ]

    def parse(self, response):
        def record(*args):
            return {
                'size': "-".join(args[0].css('span::text').extract()).strip(),
                'rating': "&lt;br/&gt;".join(args[1].css('::text').extract()).strip(),
                'outlook': args[2].css('::text').extract_first().strip(),
            }
        collector = {}
        for company in response.xpath('//table[@class="table table-bordered table3"][1]/tr'):
            row = company.css('td')
            if company.css('::attr(valign)').extract_first() == 'top':
                if collector.get('company') != None: yield collector
                collector['company'] = row[0].css('a::text').extract_first().strip()
                collector['records'] = [record(row[1], row[2], row[3])]
            elif company.css('::attr(class)').extract_first() == 'pagination-ys':
                yield collector
                pass
            else:
                collector['records'].append(record(row[0], row[1], row[2]))
