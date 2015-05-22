from Url import Url
from UrlBank import UrlBank

class PageRank():
	def __init__(self, bank, dumping, stop):
		self.bank = bank
		self.dumping = dumping
		self.stop = stop
		self.teleportation = 1-self.dumping
		self.cstop = 1
		tmpprs = {}
		for url in self.bank.urls.itervalues():
			tmpprs[url.name] = 1/float(len(self.bank.urls))
		self.setPageranks(tmpprs)
		self.printHeader()
		self.printStep(0, tmpprs, 0)

	def calculate(self):
		step = 0
		while (self.stop <= self.cstop):
			totalpr = 0
			tmpprs = {}
			for url in self.bank.urls.itervalues():
				linkjuice = 0
				for inLink in url.incoming:
					incomingUrl = self.bank.getUrl(inLink)
					linkjuice += incomingUrl.pageRank/float(len(incomingUrl.outLinks))
				for exit in self.bank.urls.itervalues():
					if (len(exit.outLinks) == 0):
						linkjuice += exit.pageRank/float(len(self.bank.urls))
				pr = (self.teleportation/float(len(self.bank.urls))) + self.dumping * linkjuice
				totalpr += abs(pr - url.pageRank)
				tmpprs[url.name] = pr
			step+=1
			self.cstop = totalpr
			self.printStep(step, tmpprs, self.cstop)
			self.setPageranks(tmpprs)

	def setPageranks(self, prs):
		for url in self.bank.urls.itervalues():
			url.pageRank = prs[url.name]

	def printHeader(self):
		print("%9s" % ("")),
		for url in self.bank.urls.itervalues():
			print("%5s%1s" % (url.title, "")),
		print("%7s" % ("diff")),

	def printStep(self, step, prs, diff):
		print("\n%s: %d [" % ("step", step)),
		for key in sorted(prs.iterkeys()):
			print("%.4f" % (prs[key])),
		print "]",
		if (diff != 0):
			print("%.4f" % (diff)),