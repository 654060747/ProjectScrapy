# windows下安装scrapy

1.新手使用如下方法下载：
- 进入网站下载：https://www.anaconda.com/distribution/　下载好后安装Anaconda

- 打开DOS输入命令：
```
conda install scrapy 
```


创建spider爬虫文件
```
scrapy genspider 爬虫名　网站域名
scrapy crawl dmoz　运行项目

```


2.再来看看传统的安装方法(不建议新手使用)：

首先时依赖包：

1、windows下安装lxml（下载之后不要改名字，要安装先进入到lxml文件所在的目录）

下载地址：http://www.lfd.uci.edu/~gohlke/pythonlibs/

使用

1
pip install lxml-3.4.4-cp27-none-win32.whl
2、安装cryptography模块

1
pip install -i http://pypi.douban.com/simple cryptography
3、安装pywin32模块

直接到http://sourceforge.net/projects/pywin32/files/pywin32/Build 20219/

下载  pywin32-219.win32-py2.7.exe

4.安装setuptools 
 用来安装egg文件，点击 这里下载python2.7的对应版本的setuptools。 

5.安装Twisted

Twisted是用Python实现的基于事件驱动的网络引擎框架，点击这里下载。

6.安装pyOpenSSL

pyOpenSSL是Python的OpenSSL接口，点击 这里下载。 

