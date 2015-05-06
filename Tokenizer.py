class Tokenizer():
	def __init__(self):
		self.tokens = {}
		self.stopWords = ['d01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd07', 'd08',  
'a', 'also', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'do',
'for', 'have', 'is', 'in', 'it', 'of', 'or', 'see', 'so',
'that', 'the', 'this', 'to', 'we']
	
	# ADD URL ELEMENT TO UPDATE ITS TOKENS
	def addUrl(self, url):
		self.name 		= url.name
		self.content 	= url.content
		# Transform to lower case
		self.content 	= self.content.lower()

		# Replacing all kinds of symbols with whitespace
		self.content 	= self.content.replace(".", " ")
		self.content 	= self.content.replace(";", " ")
		self.content 	= self.content.replace(",", " ")
		self.content 	= self.content.replace("/", " ")
		self.content 	= self.content.replace("&", " ")
		self.content 	= self.content.replace("|", " ")
		self.content 	= self.content.split()

		tmpTokens = {}
		if self.name not in self.tokens:
			for t in self.content:
				if t not in self.stopWords:
					if t not in tmpTokens:
						tmpTokens[t] = 1
					else:
						tmpTokens[t] += 1



			self.tokens[self.name] = tmpTokens
	

	def search(self, term):
		pass 

	def printMap(self):
		print self.tokens		





