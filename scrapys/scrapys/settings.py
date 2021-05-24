# -*- coding: utf-8 -*-


# scrapy.cfg：项目的配置文件
# tutorial/：项目的Python模块，将会从这里引用代码
# tutorial/items.py：项目的items文件
# tutorial/pipelines.py：项目的pipelines文件
# tutorial/settings.py：项目的设置文件
# tutorial/spiders/：存储爬虫的目录




# Scrapy settings for scrapys project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapys'

SPIDER_MODULES = ['scrapys.spiders']
NEWSPIDER_MODULE = 'scrapys.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapys (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'

# 遵守robots.txt文件中的协议，遵守允许爬取的范围
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
ROBOTSTXT_OBEY = False

# 并发量默认是16个
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 下载延迟
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 每个域名并发量
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 每个ip的并发量
#CONCURRENT_REQUESTS_PER_IP = 16

# 是否开启cookie
# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# 默认请求头
# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# 下面中间都是中间介,使用时取消注销即可
# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'scrapys.middlewares.ScrapysSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'scrapys.middlewares.ScrapysDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# 扩展中间介
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# pipelines文件需要使用时开启(用于数据清洗)
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'scrapys.pipelines.ScrapysPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 增加显示文件为中文　scrapy crawl baidu -o test.json
FEED_EXPORT_ENCODING = 'utf-8'

# 设置日志显示级别(与手动声明模块二选其一即可)
# CRITICAL - 严重错误
# ERROR - 一般错误
# WARNING - 警告信息
# INFO - 一般信息
# DEBUG - 调试信息
LOG_LEVEL = 'CRITICAL'
# 设置日志打印保存地址(结合日志级别就能打印出你想要的日志信息)
LOG_FILE = '../log/baidu.log'


#Mysql数据库的配置信息
MYSQL_HOST = '127.0.0.1'
MYSQL_DBNAME = 'user'         #数据库名字，请修改
MYSQL_USER = 'root'             #数据库账号，请修改
MYSQL_PASSWD = 'llg911025'         #数据库密码，请修改

MYSQL_PORT = 3306               #数据库端口，在dbhelper中使用
