import scrapy


class LibguidesSpider(scrapy.Spider):
    name = 'libguides'
    start_urls = [
        'http://guides.library.harvard.edu/artistsbooks',
        'http://guides.library.duke.edu/bookarts',
        'http://guides.library.cmu.edu/artistsbooks',
        'http://researchguides.uic.edu/digitalhumanities',
    ]

    def parse(self, response):

        institution = response.css('#s-lib-bc-customer > a::text').extract_first().strip()
        guide_name = response.css('#s-lg-guide-name::text').extract_first().strip()
        authors = [a.strip() for a in response.css('.s-lib-profile-name::text').extract()]
        headings = [h.strip() for h in response.css('#s-lg-guide-tabs ul li a > span::text').extract()]

        yield {
            'url': response.url,
            'institution': institution,
            'guide_name': guide_name,
            'authors': authors,
            'headings': headings
        }
