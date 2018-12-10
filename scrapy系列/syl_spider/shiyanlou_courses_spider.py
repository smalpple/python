import scrapy


class ShiyanlouCourseSpdier(scrapy.Spider):

    name = 'shiyanlou-courses'

    def start_requests(self):

        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        urls = (url_tmpl.format(i) for i in range(1, 25))

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''
    <div class="course-body">
			<div class="course-name">C语言版 Flappy Bird</div>
			<div class="course-desc">Flappy Bird 是之前十分热门的小游戏，后来出现多个衍生版本。本节课程将使用 C 语言来实现一个字符版 Flappy Bird，感受不一样的风采。本课程学习后将会熟悉C语言，以及绘图库ncurses的使用。本课程适合有C语言基础，想做练手项目的同学，可以有效的学习ncurses绘图库的使用，做一些有趣的事情。</div>
        	<div class="course-footer">
				<span class="course-per-num pull-left">
                    
                	<i class="fa fa-users"></i>
            	    5288
                	
				</span>
            	
    	            
        	            <span class="course-money pull-right">会员</span>
                    
	            
    	    </div>
       	</div>
    '''
    def parse(self, response):
        for course in response.css('div.course-body'):
            yield {
                #course-name
                'name':course.css('div.course-name::text').extract_first(),
                #course-desc
                'desc':course.xpath('.//div[@class="course-desc"]/text()').extract_first(),
                # course-type
                'type':course.css('div.course-footer span.pull-right::text').extract_first(default='Free')
            }
