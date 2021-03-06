
import scrapy

class itemSpider(scrapy.Spider):
    name = 'itemSpider'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):

        mingyan = response.css('div.quote')

        for i in range(len(mingyan)):
            text = mingyan[i].css('.text::text').extract_first()
            author = mingyan[i].css('.author::text').extract_first()
            tags = ','.join(mingyan.css('.tags .tag::text').extract())

            filename = '{}-语录.txt'.format(author)
            f = open(filename,"a+")
            f.write(text)
            f.write('\n')
            f.write('标签：'+tags)
            f.close()

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)