from UrlBank 	import UrlBank
from Url 		import Url

class IndexToken():
	
	def __init__(self, token):
		self.token = token
		self.urlList = {}

	def addUrl(self, url):
		if url.title not in self.urlList:
			tmp_tokens = url.getTokens()
			self.urlList[ url.title ] = tmp_tokens[ self.token ]

	def printToken(self):
		printable = "[";
		for url in self.urlList.iterkeys():
			printable += "(%s, %s), " % ( url, self.urlList[ url ] )
		printable = printable[:-2] + "]"
		print printable
