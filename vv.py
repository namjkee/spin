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
	
	ss=soup.findAll('div',{'class':'e_title'})
	for i in ss:
		#i.decompose()
		titless = i.h1.get_text()+"\n"
		sendprint = re.sub(r'^\s+','',titless) 
		print sendprint
		fp.write('*'*10+'-'*60+'*'*10+'\n')
		fp.write(unicode(sendprint))
		 
	ss = soup.find_all('div',{'class':'info-qh'})
	if not ss:
		fperror.write(line) 
	for i in ss:
		contentss = i.get_text()
		
		#print contentss
		for child in i.find_all('div'):#('a', {'target':'_blank'}):
	   		itext=child.get_text()
			#time.sleep(5)
			print itext
	 		fp.write(unicode(itext))
			fp.write('\n')
 
			
	ss = soup.find_all('div',{'style':'margin-bottom:4px;'})
	#print ss
	for i in ss:
		for child in i.find_all('script'):#('a', {'target':'_blank'}):
	   		itext=child.get_text()
			#time.sleep(5)
			
			m = re.search(r"Sound.*", itext)
			
			 
			if m:
				#print m.group(0)
				mp3url="http://k8.kekejp.com/"+str(m.group(0))[0:-3]
				print mp3url
				print 'the '+ str(imp3) +' are begaing...'
				print 'ok'
				print "downloading with urllib2......." 
				data = urllib2.urlopen(mp3url).read()
				
				with open(str(imp3)+".mp3", "wb") as code:
		    			code.write(data)
			
	 		#fp.write(unicode(itext))
			#fp.write('\n')





irs=8
imp3=93
line=''
fperror=''
mp3url=''
while irs<9:
	fperror = open("errortext.txt",'w+')
	read = open("a/a3/"+str(irs)+'.txt')
	
	fp = open(str(irs)+"text.txt",'w')
	
	line=read.readline()
	while line:
		print line
		url(line)
		time.sleep(1)
		imp3=imp3+1
		
		line=read.readline()#如果没有这行会造成死循环
	read.close
	fp.close()
	fperror.close()
	irs=irs+1
'''
fp = open("33text.txt",'w')
url('http://www.kekenet.com/menu/201310/260698.shtml')
fp.close()	 
	
		
	#print soup.body.extract()
	ss = soup.find_all(id="content")
	
	fp = open(sss+".txt",'w')
	for i in ss:
		
		print  i.get_text()
		#time.sleep(5)
		fp.write(unicode(i.get_text("\n")))
	




	 
line="A:Have you ever\nrun into\na \n哦哦person who\n,rr\n. rr tries\n0vleed yo\n'u white?你有没有n\n...j\n  遇到一个把你榨干的一个人？\nB:I am always\non the look out for\nsuch girls."
	
line= re.sub(r"\b\n([a-z|A-Z|0-9|\W])",r" \1",line)
print line
time.sleep(10)

'''		 


