#python学习过程记录## Day1 爬虫的基本原理：* 通过url获取数据；* 输入网址-dns服务器解析域名-服务器主机-get请求* URL 统一资源定位符 就是我们说的网址 由 协议  IP地址  和 资源具体位置构成
##Day2
###urllib库使用：
* 导入urllib库 import urllib.request
* 打开网址 res=urllib.request.urlopen(url)
* 读取结果 html=res.read()
###python装饰器：
* 不改变原来的函数结构，并添加其他功能；
* 语法是在以前的函数定义处添加一个@装饰器函数的名字
#TODO* scrapy库了解