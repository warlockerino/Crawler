from Tokenizer import Tokenizer 

class Url():
	def __init__(self, link, pagetitle, outgoing, html):
		self.name 		= link
		self.title 		= pagetitle
		self.outLinks 	= {}
		self.incoming	= {}
		self.content	= html
		self.pageRank   = 1
		t	 			= Tokenizer(self.content) 
		self.tokens 	= t.getTokens()
		
		for ol in outgoing:
			self.addOut(ol)

	def addIn(self, host):
		if host in self.incoming:
			self.incoming[host] += 1

		else:
			self.incoming[host] = 1 

	def addOut(self, dest):
		if dest in self.outLinks:
			self.outLinks[dest] += 1
		else:
			self.outLinks[dest] = 1

	def getTokens(self):
		return self.tokens

	def notify(self, newLinks, newSide):
		counter = 0
		if self.name in newLinks:
			for x in range(0, newLinks[self.name]):
				self.addIn(newSide)
		if newSide in self.outLinks:
			counter = self.outLinks[newSide]
		return counter

	def printOut(self):
		printable = ""
		for o in self.outLinks:
			u = o.replace("/", " ")
			u = u.split()
			printable += "%s," % (u[-1].replace(".html", ""))
		printable = printable[:-1]
		return printable

	def printCon(self):
		print self.title
		print "outgoing :",len(self.outLinks)
		print "incoming :",len(self.incoming)
		print("Pagerank: %.4f" % self.pageRank),"\n"
		print self.tokens
