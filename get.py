#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2,time,os
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
i=1
origal="http://www.kekenet.com/menu/14317/List_"

def urlopen(u):
	#14317必背英文面试口语
	#userMainUrl = "http://www.kekenet.com/menu/13341/"; #http://www.kekenet.com/menu/13341/List_1.shtml 迷你英语情景对话学口语
	try:
		req = urllib2.Request(u);
		resp = urllib2.urlopen(req);
		page = resp.read();
	except Exception as e:
		return
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
	links=soup.findAll('div',{'class':'list_box_2'}) 
	for iss in links: 
		#print i.ul.li.h2.a['href']
	
		#print range(len(i.ul.contents),-1,-1)
	 	fp = open('a/a3/'+str(i)+".txt",'w')
		#fp = open('a/a3/36'+".txt",'w')
		for child in iss.ul.find_all('h2'):#('a', {'target':'_blank'}):
	   		itext='http://www.kekenet.com'+child.a['href']+'\n'
			print itext
			fp.write(unicode(itext))
			
		fp.close()

while i<8:
	'''try:
		os.makedirs('a/'+'a'+str(i))
	except Exception as e:
		print 'oo'
	'''
	userMainUrl=origal+str(i)+".shtml"
	
	print userMainUrl
	urlopen(userMainUrl)
	i=i+1
	time.sleep(1)



	#doc = BeautifulSoup(open(“test.html”))


''''
    ##判断tag是a的里面，href是否存在。 
    if 'href' in str(i): 
        linkname=i.string 
        linkaddr=i['href'] 
        if 'NoneType' in str(type(linkname)):#当i无内容是linkname为Nonetype类型。 
            print linkaddr 
        else: 
            print linkname+'\n-------->http://www.kekenet.com'+linkaddr 
 
soup = BeautifulSoup(page)
 

 
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
