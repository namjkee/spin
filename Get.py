#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import urllib2
from bs4 import BeautifulSoup
#doc = BeautifulSoup(open(“test.html”))
userMainUrl = "http://www.kekenet.com/menu/13619/";
req = urllib2.Request(userMainUrl);
resp = urllib2.urlopen(req);
page = resp.read();
#print "respHtml=",page; # you should see the ouput html
#page = urllib2.urlopen('http://www.51voa.com/Word_Master_1.html');
#doc = BeautifulSoup(page,fromEncoding="gb18030")
soup = BeautifulSoup(page)
#print  soup.find('div',id='right_box').find('div',id='right_box_title').find('div',id='list')
#print soup.prettify()
#print soup.find('div',id='list')
#soup=soup.find('div',id='list')
#print soup.li.a.get_text(), soup.li.a['href'] 
#soup=soup.find('div', {'id':'list'})
links=soup.findAll('a',{'target':'_blank'}) 
for i in links: 
    ##判断tag是a的里面，href是否存在。 
    if 'href' in str(i): 
        linkname=i.string 
        linkaddr=i['href'] 
        if 'NoneType' in str(type(linkname)):#当i无内容是linkname为Nonetype类型。 
            print linkaddr 
        else: 
            print linkname+'\n-------->http://www.51voa.com'+linkaddr 
 ''' 
soup = BeautifulSoup(page)

time.sleep(56)
 
#这样也可以，比较方便：
div = soup.find('div', {'id':'title'})
print div.string #找出标题
div = soup.find('a', {'id':'mp3'})
print div['href'] #找出MP3
#--------------------------------
#这样也可以，比较方便：
div = soup.find('a', {'target':'_blank'})
print  div['href'] #找出标题
print  div.string #找出标题 

print  div.string+'\nhttp://www.51voa.com' + div['href']
print  
 '''
