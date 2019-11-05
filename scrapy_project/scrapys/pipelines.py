# -*- coding: utf-8 -*-
import pymysql
from scrapy.exceptions import DropItem

class ScrapysPipeline(object):
	"""数据过滤"""
	def process_item(self, item, spider):
		if item['name'] == '百一下':
		# if item['name'] == '百度一下':
			raise DropItem("Drop item found: %s" % item)
		else:
			return item


class MysqlPipeline(object):
	"""mysql操作"""
	def __init__(self,host,db,user,passwd,port):
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db
		self.client = None
		self.cursor = None

	# 从配置文件拿数据注入初始化
	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			host = crawler.settings.get("MYSQL_HOST"),
			port = crawler.settings.get("MYSQL_PORT"),
			user = crawler.settings.get("MYSQL_USER"),
			passwd = crawler.settings.get("MYSQL_PASSWD"),
			db = crawler.settings.get("MYSQL_DBNAME"),
			)

	# 链接数据库
	def open_spider(self,spider):
		self.client = pymysql.connect(
			host = self.host,
			port = self.port,
			user = self.user,
			passwd = self.passwd,
			db = self.db,
			charset = 'utf8',
			cursorclass = pymysql.cursors.DictCursor
			)
		self.cursor = self.client.cursor()
		spider.logger.info('open_spider: %s' % "===============成功链接数据库")

	# 数据库操作
	def process_item(self, item, spider):
		# 向数据库中插入数据
		sql = 'insert into baidu(name,a,b,c) VALUES (%s,%s,%s,%s)'
		lis = (item['name'],item['a'],item['b'],item['c'])
		try:
			self.cursor.execute(sql,lis)
			self.client.commit()
		except Exception:
			spider.logger.warning('open_spider: %s' % "=============提交数据库失败")

		return item

	# 关闭数据库
	def close_spider(self,spider):
		self.client.close()
		spider.logger.info('open_spider: %s' % "==============成功关闭数据库")
