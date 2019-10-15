# -*- coding: utf-8 -*-
import scrapy
from doubleScrapy.items import DoublescrapyItem


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'  #爬虫名字
    allowed_domains = ['movie.douban.com']  # 允许的域名
    start_urls = ['https://movie.douban.com/top250'] # 入口url，丢到调度里去

    def parse(self, response):
        """对请求回来的信息进行解析"""
        movieList = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for item in movieList:
            douban_item = DoublescrapyItem()
            douban_item['serial_number'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            douban_item['introduce'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['star'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['evaluate'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['describe'] = item.xpath(".//div[@class='item']//em/text()").extract_first()

            print(douban_item)

