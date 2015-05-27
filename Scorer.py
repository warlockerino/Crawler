from UrlBank 	import UrlBank
from Url 		import Url
from Tokenizer	import Tokenizer
from Index		import Index
import math

class Scorer():
	def __init__(self, phrase, index):
		self.tokens = Tokenizer( phrase )
		self.index = index
		self.ranking = {}
		self.calc_ranking()

	def calc_ranking(self):

		tcounts = {}
		lengths = {}
		tlengths = 0

		for t in self.tokens.getTokens():
			
			if t not in tcounts:
				tcounts[ t ] = 0
			tcounts[ t ] += 1

		for t in self.tokens.getTokens():
			it = self.index.getIndexToken( t )
		
			tcount = 0
			for d in it.urlList.iterkeys():
				tcount += it.urlList[ d ]

			dtf = math.log10( float( len( self.index.bank.urls ) ) / float( self.index.getDocumentFrequency( t ) ) )

			for d in it.urlList.iterkeys():
				
				tf = ( 1 + math.log10( it.urlList[ d ] ) )
				wtq = tf * dtf
				wtd = ( 1 + math.log10( tcounts[ t ] ) ) * dtf
				
				if d not in self.ranking:
					self.ranking[ d ] = 0

				self.ranking[ d ] += ( wtq * wtd ) / ( math.sqrt( math.pow( wtq, 2 ) ) * math.sqrt( math.pow( wtd, 2 ) ) )

		for i in self.index.index:
			urls = self.index.index[ i ].urlList
			for d in urls.iterkeys():
				if d not in lengths:
					lengths[ d ] = 0
				lengths[ d ] += math.pow( ( 1 + math.log10( urls[ d ] ) ) * math.log10( float( len( self.index.bank.urls ) ) / float( self.index.getDocumentFrequency( i ) ) ), 2 )

		print "\nDokumentenlaengen:\n"

		for d in lengths:
			lengths[ d ] = math.sqrt( lengths[ d ] )
			print("%.6f" % (lengths[d]))

		for t in self.tokens.getTokens():
			tlengths += math.pow( ( 1 + math.log10( tcounts[ t ] ) ) * math.log10( float( len( self.index.bank.urls ) ) / float( self.index.getDocumentFrequency( i ) ) ), 2 )

		tlengths = math.sqrt( tlengths )

		for d in self.ranking:
			self.ranking[ d ] = self.ranking[ d ] / ( lengths[ d ] * tlengths )

		for d in self.ranking:
			print d, ": ", self.ranking[d]

	def calc_tf(self):
		tf = self.search_token(tokens, term)
		tf = (1 + math.log10(tf)) 
		return tf

	def calc_dtf(self, term, UrlBank):
		freq 		= 0
		N 			= 0 
		for u in UrlBank.urls.keys():
			N += 1
			holds 	= self.calc_tf(UrlBank.urls[u], term)
			if holds > 0:
				freq += 1
		# must return log10 (urlbank.size() / freq)
		freq = math.log10(N / freq)
		return freq


	def calc_weight(self, tf, dtf):
		return tf * dtf

	def calc_score(self, w_t_qbb, w_t_d):
		score = (w_t_q * w_t_d) / (math.sqrt(math.pow(w_t_q, 2)) * math.sqrt(math.pow(w_t_d,2)))

	def search_token(self, tokens, term):
		token = 0
		for k in tokens:
			for v in tokens[k]:
				if term in v:
					token = tokens[v]
		return token
