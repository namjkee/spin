#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
def url(u):
	req = urllib2.Request(u);
	resp = urllib2.urlopen(req);
	page = resp.read();
	 
	soup = BeautifulSoup(page)
	ss = soup.find_all(id="title")
	for i in ss:
		ss = i.get_text()
	ss=ss.replace("\'","")
	ss=ss.replace("?","")
	ss=ss.replace("\"","")
	ss=ss.replace("[","")
	ss=ss.replace("]","")
	ss=ss.replace(",","")
	sss=ss.replace("[","")
	
	print  ss
	#time.sleep(50)
	ss = soup.find_all(id="playbar")
	for i in ss:
		i.decompose()
	 
	ss = soup.find_all(id="mp3")
	for i in ss:	 
		print "downloading with urllib2" 
		data = urllib2.urlopen(str(i['href'])).read()
		with open(sss+".mp3", "wb") as code:
    			code.write(data)
		
		
	#print soup.body.extract()
	ss = soup.find_all(id="content")
	
	fp = open(sss+".txt",'w')
	for i in ss:
		
		print  i.get_text()
		#time.sleep(5)
		fp.write(unicode(i.get_text("\n")))
	fp.close()



read = open("t")
line=read.readline()
while line:
	print line
	url(line)
	time.sleep(5)
	line=read.readline()#如果没有这行会造成死循环
read.close



