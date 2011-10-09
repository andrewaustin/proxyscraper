#!/usr/bin/python
import urllib2
import urllib
import re
import socket

#the list of all the Proxies
list = []

#The following is so we look like we are a google bot...not sure if it actually matters.
user_agent = 'Agent: Googlebot/2.1 (+http://www.googlebot.com/bot.html)'

def getProxyList():
	the_url= 'http://www.digitalcybersoft.com/ProxyList/fresh-proxy-list.shtml'
	data = urllib.urlencode({'submit': 'submit'})
	req = urllib2.Request(the_url)
	req.add_header('User-Agent', user_agent)
	handle = urllib2.urlopen(req)
	the_page = handle.read()

	ProxyList = re.compile(r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4]      \
[0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):([0-9]+)\b', re.IGNORECASE | re.DOTALL)
	lines = ProxyList.findall(the_page)
		
	for x in lines:
		list.append(x[0] + '.' + x[1] + '.' + x[2] + '.' + x[3] + ':' + x[4])		

#get Proxies
getProxyList()
#save proxies
good = []
for x in list:
	print x, "..."
       	try:
		port_index = x.find(":")
		if x >= 0:
			address = x[0:port_index]
			port = x[port_index + 1:]
		else:
			address = x
			port = "80"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(5)
		s.connect((address, int(port)))
                f = open("proxies.txt", "a")
                f.write(x + "\n")         	
                f.close()
                s.close()
	except Exception, e:
		print "Could not connect!", e
