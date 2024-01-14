import scrapy
from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_SPIDER_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_SPIDER_URL]
    start_urls = [f'https://{PEP_SPIDER_URL}/']

    def parse(self, response):
        for link in response.css('tbody tr a[href^="pep-"]'):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title_parts = response.css('h1.page-title::text').get().split()
        number = title_parts[1] if len(title_parts) > 1 else None
        name = ' '.join(title_parts[2:]).strip()

        data = {
            'number': number,
            'name': name,
            'status': response.css(
                'dt:contains("Status")+dd abbr::text'
            ).get()
        }
        yield PepParseItem(data)

