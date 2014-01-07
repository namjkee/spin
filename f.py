#========================================================
#          			 2013/09/2 
#			http://blog.csdn.net/agoago_2009             
#========================================================
# -*- coding:utf-8 -*-

import urllib2,cookielib,urllib,re,random,json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')	
class FEIXIN:
	
	def __init__(self):
	
		print 'init FEIXIN class...'
		
		self.name = "18790349273"
		self.passwd = 'woaiceo123'
		
		ckjar = cookielib.CookieJar()
		cookiehandle = urllib2.HTTPCookieProcessor(ckjar)
		self.opener = urllib2.build_opener(cookiehandle)
		urllib2.install_opener(self.opener)
		
		self.ssid = ''
		self.uid = ''
		self.counter = 0
		
		self.login()
		self.GetPersonalInfo()

	def login(self):
		print 'start to login...'
		
		req = urllib2.Request("https://webim.feixin.10086.cn/WebIM/Login.aspx")

		req.add_header("x-requested-with", "XMLHttpRequest")
		req.add_header("Accept-Language", "zh-cn")
		req.add_header("Referer", "https://webim.feixin.10086.cn/loginform.aspx")
		req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
		req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
		#req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)")
		req.add_header("Connection", "Keep-Alive")
		req.add_header("Cache-Control", "no-cache")

		body = r"UserName=" + self.name + "&Pwd=" + self.passwd + "&OnlineStatus=400&AccountType=1"

		conn = self.opener.open(req,body)
		info = conn.info()
		#print info['Set-Cookie']
		self.ssid = info['Set-Cookie'].split("webim_sessionid=")[1].split(";")[0]
		print self.ssid
		data = conn.read()
		#print data
		if '{"rc":200}' == data:
			print 'login succeessfully...'
		
		
	def GetPersonalInfo(self):
		print 'GetPersonalInfo...'
		req = urllib2.Request("https://webim.feixin.10086.cn/WebIM/GetPersonalInfo.aspx?Version="+ str(self.counter))
		self.counter = self.counter + 1

		req.add_header("x-requested-with", "XMLHttpRequest")
		req.add_header("Accept-Language", "zh-cn")
		req.add_header("Referer", "https://webim.feixin.10086.cn/main.aspx")
		req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
		req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
		#req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)")
		req.add_header("Connection", "Keep-Alive")
		req.add_header("Cache-Control", "no-cache")

		body = r"ssid=" + self.ssid

		conn = self.opener.open(req,body)
		info = conn.info()
		data = conn.read()
		data = json.loads(data)
		
		self.uid = str(data["rv"]["uid"])
		return data
		
	def GetContactList(self):
		print 'GetContactList...'
		req = urllib2.Request("https://webim.feixin.10086.cn/WebIM/GetContactList.aspx?Version="+ str(self.counter))
		self.counter = self.counter + 1

		req.add_header("x-requested-with", "XMLHttpRequest")
		req.add_header("Accept-Language", "zh-cn")
		req.add_header("Referer", "https://webim.feixin.10086.cn/main.aspx")
		req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
		req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
		#req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)")
		req.add_header("Connection", "Keep-Alive")
		req.add_header("Cache-Control", "no-cache")

		body = r"ssid=" + self.ssid

		conn = self.opener.open(req,body)
		info = conn.info()
		data = conn.read()
		data = json.loads(data)
		return data

	def GetFriendUid(self,user_name):
		data = api.GetContactList()
		friends = data["rv"]["bds"]
		for friend in friends:
			name = friend["ln"]
			uid = str(friend["uid"])
			if name.encode("utf8") == user_name:
				print name,uid
				return uid
		return '0'
	
	
	def GetPcRecommendBuddyListV2Handler(self):
		print 'GetPcRecommendBuddyListV2Handler...'
		req = urllib2.Request("https://webim.feixin.10086.cn/WebIM/GetPcRecommendBuddyListV2Handler.aspx?Version="+ str(self.counter))
		self.counter = self.counter + 1

		req.add_header("x-requested-with", "XMLHttpRequest")
		req.add_header("Accept-Language", "zh-cn")
		req.add_header("Referer", "https://webim.feixin.10086.cn/main.aspx")
		req.add_header("Accept", "application/json, text/javascript, */*; q=0.01")
		req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
		#req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)")
		req.add_header("Connection", "Keep-Alive")
		req.add_header("Cache-Control", "no-cache")

		body = r"ssid=" + self.ssid

		conn = self.opener.open(req,body)
		info = conn.info()
		data = conn.read()
		data = json.loads(data)
		return data

	def SendSMS(self,Receivers,Message):
		#Receivers = [669456576,649237761]
		#Receivers = ','.join(Receivers)
		print 'SendSMS...'
		req = urllib2.Request("https://webim.feixin.10086.cn/content/WebIM/SendSMS.aspx?Version="+ str(self.counter))
		self.counter = self.counter + 1

		req.add_header("x-requested-with", "XMLHttpRequest")
		req.add_header("Accept-Language", "zh-cn")
		req.add_header("Referer", "https://webim.feixin.10086.cn/content/freeSms.htm?tabIndex=0")
		req.add_header("Accept", "application/json, text/javascript, */*")
		req.add_header("Content-Type", "application/x-www-form-urlencoded")
		#req.add_header("Accept-Encoding", "gzip, deflate")
		req.add_header("User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)")
		req.add_header("Connection", "Keep-Alive")
		req.add_header("Cache-Control", "no-cache")

		body = r"UserName=" + self.uid + "&Message=" + urllib.quote(Message) + "&Receivers=" + Receivers + "&ssid=" + self.ssid

		conn = self.opener.open(req,body)
		info = conn.info()
		data = conn.read()
		data = json.loads(data)
		return data	
		

if __name__=="__main__":
	
	api = FEIXIN()
	
	api.SendSMS(api.uid,'send to myself to test...')


