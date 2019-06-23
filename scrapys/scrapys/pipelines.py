# -*- coding: utf-8 -*-
import pymysql
from scrapy.utils.project import get_project_settings
import logging



# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ScrapysPipeline(object):


	# 构造方法初始化
	def __init__(self):
		# 初始化settings
		self.settings = get_project_settings()
		self.client = pymysql.connect(

				host = self.settings['MYSQL_HOST'],
		        port = self.settings['MYSQL_PORT'],
		        user = self.settings['MYSQL_USER'],
		        passwd = self.settings['MYSQL_PASSWD'],
		        db = self.settings['MYSQL_DBNAME'],
		        charset = 'utf8',
		        cursorclass = pymysql.cursors.DictCursor

			)
		self.cur = self.client.cursor()	
		# self.cur.execute("DROP TABLE IF EXISTS baidu")
		# sql = "CREATE TABLE baidu (id INT auto_increment primary key not null,name CHAR(20) NOT NULL,a CHAR(20),b CHAR(20),  c CHAR(20))"
		# self.cur.execute(sql)

	def process_item(self, item, spider):
		# 数据清洗去重等操作
        # name = item['name']
        # if name:
        #     item['name'] = name.strip().replace('\n','').replace(' ','')
        # a = item['a']
        # if a:
        #     item['a'] = a.replace('\xa0','')
        # content = item['content']

		# 插入数据库
		with self.cur as cur:
			print("=============数据库插入============")
			sql = 'insert into baidu(name,a,b,c) VALUES (%s,%s,%s,%s)'
			lis = (item['name'],item['a'],item['b'],item['c'])
			try:
				cur.execute(sql,lis)
				self.client.commit()
			except Exception:
				print("提交数据库失败")

		return item
