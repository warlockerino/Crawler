from Url import Url

class UrlBank():
	def __init__(self):
		self.urls = {}
		self.counter = 0

	def addRoots(self, rootUrls):
		for u in rootUrls:
			self.counter += 1
			self.addUrl(u)

	# Since were doin it quick n dirty : 
	def getNext(self):
		if self.counter < len(self.urls):
			return self.urls[self.counter - 1]
		else:
			counter = 0
			return 0

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

	def sortBank(self):
		self.urls = collections.OrderedDict(sorted(self.urls.items()))