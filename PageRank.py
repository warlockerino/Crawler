from Url import Url
from UrlBank import UrlBank

class PageRank():
	def __init__(self, bank, dumping, stop):
		self.bank = bank
		self.dumping = dumping
		self.stop = stop
		self.teleportation = 1-self.dumping
		self.cstop = 1

	def calculate(self):
		step = 0
		while (self.stop <= self.cstop):
			print "step",step
			totalpr = 0
			for url in self.bank.urls.itervalues():
				pr = float(1)
				if (step == 0):
					pr = 1/float(len(self.bank.urls))
				else:
					pr = (self.teleportation/float(len(self.bank.urls)))
					linkjuice = 0
					for inLink in url.incoming:
						incomingUrl = self.bank.getUrl(inLink)
						linkjuice += incomingUrl.pageRank/float(len(incomingUrl.outLinks))
					for exit in self.bank.urls.itervalues():
						if (len(exit.outLinks) == 0):
							linkjuice += exit.pageRank/float(len(self.bank.urls))
					tmppr = pr
					pr = pr + self.dumping * linkjuice
					print "PR for ",url.name,"=",tmppr,"+ (",self.dumping,"*",linkjuice,") =",pr
				totalpr += abs(pr - url.pageRank)
				url.pageRank = pr
			step+=1
			self.cstop = totalpr
			print "Current stop value:",self.cstop