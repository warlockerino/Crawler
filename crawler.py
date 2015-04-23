import urllib
import re

stcokNames = [ "aapl", "spy", "goog","nflx"]
urls = ["http://finance.yahoo.com/q?s=AAPL&q-l=1"]

regex = '<title>(.+?)</title>'

for stocks in stcokNames:
	url = "http://finance.yahoo.com/q?s="+ stocks +"&q-l=1"
	htmlfile = urllib.urlopen(url)
	htmltext =htmlfile.read()
	regex = '<span id="yfs_l84_'+ stocks + '">(.+?)</span>'
	pattern = re.compile(regex)
	title = re.findall(pattern,htmltext)
	print " ", stocks, "\t : " , title
	#tags

