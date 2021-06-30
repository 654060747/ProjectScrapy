# -*- coding: utf-8 -*-

# Spider Middleware有如下三个作用。
# 我们可以在Downloader生成的Response发送给Spider之前，也就是在Response发送给Spider之前对Response进行处理。
# 我们可以在Spider生成的Request发送给Scheduler之前，也就是在Request发送给Scheduler之前对Request进行处理。
# 我们可以在Spider生成的Item发送给Item Pipeline之前，也就是在Item发送给Item Pipeline之前对Item进行处理。


# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from random import choice
from scrapy import signals
# pip install fake-useragent -i https://pypi.douban.com/simple
from fake_useragent import UserAgent


class ScrapysSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapysDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ProxyMiddleware(object):
    '''添加代理'''
    def process_request(self, request, spider):
        # 代理ip
        proxy_list = [
            "https://222.89.32.182:9999",
            "http://117.95.214.219:9999",
            "http://180.122.38.203:9999",
            "https://49.89.103.230:9999",
            "http://183.164.238.132:9999",
            "http://123.232.153.28:8118",
            "http://183.154.49.158:9999",
            "http://183.164.239.174:9999",
            "http://117.57.90.212:9999",
            "http://110.85.58.169:808",
            "http://117.94.245.73:9999",
            "http://117.28.97.196:9999",
            "http://117.69.201.41:9999",
            "http://112.84.178.21:8888",
            "https://27.152.90.97:9999",
            "http://183.166.7.201:9999",
            "https://117.69.201.78:9999",
            "https://117.69.201.125:9999",
            "http://219.157.144.198:8118",
            "https://183.154.52.6:9999",
            "https://27.152.91.165:9999",
            "http://119.27.161.150:8080",
            "http://14.115.107.158:808",
            "https://61.128.208.94:3128",
            "https://120.78.225.5:3128",
            "https://123.139.56.238:9999",
            "https://218.60.8.99:3129",
            "https://123.59.211.215:3128",
            "https://182.61.175.77:8118",
            "http://139.199.19.174:8118",
            "https://27.191.234.69:9999",
            "http://118.31.79.90:3128",
            "http://221.122.91.59:80",
            "https://59.38.60.252:9797",
            "https://42.228.3.158:8080",
            "http://218.66.253.146:8800",
            "http://218.66.253.145:8800",
            "http://218.66.253.144:8800",
            "http://183.136.177.77:3128",
            "https://116.62.213.167:3128",
            "https://49.51.155.45:8081",
            "https://116.204.152.110:8080",
            "http://116.196.90.176:3128",
            "http://1.196.161.46:9999",
            "https://139.224.21.138:80",
            "http://202.112.51.51:8082",
            "http://121.10.141.149:8080",
            "http://118.89.44.224:8118",
            "https://59.57.148.2:9999",
            "https://106.110.212.67:9999",
            "https://124.89.2.250:63000",
            "https://117.69.200.253:9999",
            "https://27.152.90.97:9999",
            "https://121.40.119.149:3128",
            "https://59.57.149.88:9999",
            "https://49.85.179.179:9999",
            "https://124.237.83.14:53281",
            "https://59.57.148.151:9999",
            "https://27.152.91.165:9999",
            "https://59.57.149.131:9999",
            "https://120.78.225.5:3128",
            "https://59.57.148.216:9999",
            "https://182.35.87.89:9999",
            "https://114.239.1.50:9999",
            "https://183.164.239.87:9999",
            "https://27.152.91.48:9999",
            "https://123.169.169.121:9999",
            "https://182.35.86.48:9999",
            "https://183.164.239.47:9999",
            "https://114.239.250.117:9999",
            "https://113.109.249.32:808",
            "http://120.83.106.4:9999",
            "http://117.57.90.242:9999",
            "http://180.122.38.203:9999",
            "http://125.78.177.176:9999",
            "http://117.57.91.142:9999",
            "http://123.163.97.187:9999",
            "http://117.95.174.172:9999",
            "http://183.154.49.158:9999",
            "http://117.57.91.61:9999",
            "http://183.164.239.60:9999",
            "http://110.85.58.169:808",
            "http://14.115.107.158:808",
            "http://112.84.178.21:8888",
            "http://27.152.90.52:9999",
            "http://183.164.238.162:9999",
            "http://183.164.238.79:9999",
            "http://219.157.144.198:8118",
            "http://113.120.35.12:9999",
            "http://119.27.161.150:8080",
            "http://183.164.238.91:9999",
            "http://182.35.87.15:9999",
            "http://114.239.253.64:9999",
            "http://183.164.238.137:9999",
            "http://117.57.91.54:9999",
            "http://106.14.206.26:8118",
            "http://182.35.83.150:9999",
        ]
        #1.使用python random模块的choice方法随机选择某个元素
        proxy_ip = choice(proxy_list)
        print(proxy_ip)
        request.meta['proxy'] = proxy_ip


class UserAgentMiddleware(object):
    '''伪装浏览器'''
    def process_request(self, request, spider):
#         ua_list = [
#             "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#             "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#             "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#             "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#             "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#             "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#             "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#             "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#             "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#             "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#             "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
#             "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
#             "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
#             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#             "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
#             "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
#             "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#             "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#             "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#             "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
#             "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
#             "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
#             "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
#             "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
#             "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
#         ]
#         agent = choice(ua_list)
        User_Agent = UserAgent()
        agent = User_Agent.random
        print(agent)
        request.headers['User-Agent'] = agent
