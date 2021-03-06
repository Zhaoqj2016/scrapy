import scrapy

class xssl(scrapy.Spider):
    name = "xssl"
    start_urls=["http://mp.weixin.qq.com/profile?src=3&timestamp=1468992874&ver=1&signature=SQel6cxwN1hVgtAfu8aSeLTed*aEPQELb0rbOsKL51i4ab3nY4YD2hIuRsevb7ZbqM8vShkH9W4LhyTjJ8WXDA=="]

    def parse(self,response):
        print(123)
        html = response.read().decode('utf-8')
        print(html)
				
        for href in  response.css('.question-summary .summary h3 a::attr(href)'):
            full_url =response.urljoin(href.extract())
            print(full_url)
            yield scrapy.Request(full_url,callback=self.parse_question)

    def parse_question(self,response):
        yield {
            "title":response.css('.container  a::text').extract()[0],
            "votes":response.css(".question .vote-count-post::text").extract()[0],
            "body":response.css(".question .post-text").extract()[0],
            "tags":response.css(".queston .post-tag::text").extract(),
            "link":response.url,
        }