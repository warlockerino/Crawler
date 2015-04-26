from Url import Url

class UrlBank():
	def __init__(self):
		self.urls = {}

	def addUrl(self, url):
		if url.name not in self.urls:
			self.urls[url.name] = url 
		for u in self.urls.itervalues():
			counter = u.notify(url.outLinks, url.name)
			for x in range(0,counter):
				url.addIn(u.name)

	def printBank(self):
		for key in sorted(self.urls.iterkeys()):
			self.urls[key].printCon()

	def getUrl(self, url):
		if (self.urls.get(url)):
			return self.urls.get(url)
		return 0