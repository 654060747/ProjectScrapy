# -*- coding: utf-8 -*-
import scrapy
from scrapys.items import ScrapysItem

# https://www.anaconda.com/
# conda install scrapy 
# scrapy genspider 爬虫名　网站域名
# scrapy crawl 爬虫名　运行项目
class BaiduPySpider(scrapy.Spider):
	# 爬虫名
	name = 'baidu'
	# 允许的域名
	allowed_domains = ['www.baidu.com']
	# 入口url,扔到调度器里面去
	start_urls = ['https://www.baidu.com/']

	# 默认解析方法
	def parse(self, response):
		baidu_item = ScrapysItem()
		# xpath取属性值@value 取文本值text()
		baidu_item['name'] = response.xpath('//*[@id="su"]/@value').extract_first()
		baidu_item['a'] = response.xpath('//*[@id="mMenu"]/li[1]/a/text()').extract_first()
		# css取文本值::text 取属性值::attr(title)
		baidu_item['b'] = response.css('#mMenu > li:nth-child(2) > a::text').extract()
		baidu_item['c'] = response.css('#su::attr(value)').extract_first()
		# print(baidu_item)
		# 将数据yield到pipelines里面进行数据清洗存储等
		yield baidu_item



