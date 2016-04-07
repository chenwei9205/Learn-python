#coding=utf-8
from urllib import request
import re

url="http://www.heibanke.com/lesson/crawler_ex00/";
stop=0;
def getinfo(url):
	html=request.urlopen(url).read().decode("utf-8")
	print(url)
	reg=r'/d{5}'
	reg=re.compile(reg)
	num=re.search(reg,html);
	print(num)
	if not num:
		stop=1;
	else:
		url=reg.sub(url,num);
while stop==0:
	print(url)
	getinfo(url);
