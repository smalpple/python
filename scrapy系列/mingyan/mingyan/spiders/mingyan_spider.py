import scrapy

class mingyan(scrapy.Spider):

    name = "mingyan22"
    start_urls = [  #代替start_requests方法
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]

    # def start_requests(self):
    #
    #     urls = [
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):

        page = response.url.split('/')[-2]
        filename = 'mingyan-{}.html'.format(page)
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('保存文件：{}'.format(filename))
