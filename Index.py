from UrlBank 	import UrlBank
from Url 		import Url
from IndexToken import IndexToken

class Index():
	
	def __init__(self, bank):
		self.bank = bank
		self.index = {}
		for url in self.bank.urls.itervalues():
			for token in url.getTokens().iterkeys():
				if token not in self.index:
					self.index[ token ] = IndexToken( token )
				self.index[ token ].addUrl( url )

	def printIndex(self):
		for token in sorted(self.index.iterkeys()):
			print("(%s, df:%s) ->" % (token, self.getDocumentFrequency(token))),
			self.index[ token ].printToken()

	def getDocumentFrequency(self, token):
		if token in self.index:
			return len(self.index[ token ].urlList)
		return 0
