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
	ss = soup.find_all(id="article")
	if not ss:
		fperror.write(line) 
	for i in ss:
		contentss = i.get_text("\n")
		
	#print re.sub(r'^\s+','',contentss)
	
	#time.sleep(50)
	ss=soup.findAll('div',{'class':'e_title'})
	for i in ss:
		#i.decompose()
		titless = i.h1.get_text()+"\n"
		sendprint = re.sub(r'^\s+','',titless)+re.sub(r'^\s+','',contentss)+'\n'
		#sendprint= re.sub(r"\s[:]\n",":",sendprint)
		#sendprint= re.sub(r"(\w+)\n", lambda m: ' '+m.group(1),sendprint)
		#sendprint= re.sub(r"(\n\w+.*)\n",r"\1",sendprint)
		#sendprint= re.sub(r"(\W*)\n\W\s+",r"\1",sendprint)
		sendprint= re.sub(r"\s([:\.?])\n",r"\1",sendprint)
		sendprint= re.sub(r"\b\n([a-zA-Z0-9\W])",r" \1",sendprint)
		print sendprint
		fp.write(unicode(sendprint))
		fp.write('-'*80+'\n')
	 
	'''	
		
	#print soup.body.extract()
	ss = soup.find_all(id="content")
	
	fp = open(sss+".txt",'w')
	for i in ss:
		
		print  i.get_text()
		#time.sleep(5)
		fp.write(unicode(i.get_text("\n")))
	

'''
i=25
line=''
fperror = open("errortext.txt",'w')
while i<37:
	
	read = open("a/a1/"+str(i)+'.txt')
	
	fp = open(str(i)+"text.txt",'w')
	i=i+1
	line=read.readline()
	while line:
		print line
		url(line)
		time.sleep(1)
		line=read.readline()#如果没有这行会造成死循环
	read.close
	fp.close()
fperror.close()



