#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup
#doc = BeautifulSoup(open(“test.html”))

userMainUrl = "http://www.51voa.com/Word_Master_2.html";
req = urllib2.Request(userMainUrl);
resp = urllib2.urlopen(req);
page = resp.read();
 
soup = BeautifulSoup(page)

 
#这样也可以，比较方便：
ss = soup.find_all('a', {'target':'_blank'})
#print  div['href'] #找出标题
#print  div.string #找出标题 
fp = open("test.txt",'w') 
for i in ss:
	print  "http://www.51voa.com" + i['href']
        fp.write("http://www.51voa.com" + i['href']+"\n")
fp.close()
 


 
 


 
