from UrlBank 	import UrlBank
from Url 		import Url
from Tokenizer	import Tokenizer
from Index		import Index
import math
import operator

class Scorer():
	
	def __init__(self, phrase, index):
		self.tokens = Tokenizer( phrase )
		self.index = index
		self.ranking = {}
		self.lengths = {}
		self.tlength = 0
		self.calc_document_length()
		self.calc_query_length()
		self.calc_ranking()

	def calc_document_length(self):
		for i in self.index.index:
			urls = self.index.index[ i ].urlList
			for d in urls.iterkeys():
				if d not in self.lengths:
					self.lengths[ d ] = 0
				self.lengths[ d ] += math.pow( self.calc_tf( urls[ d ] ) * self.calc_dtf( len( self.index.bank.urls ), i ), 2 )
		for d in self.lengths:
			self.lengths[ d ] = math.sqrt( self.lengths[ d ] )

	def calc_query_length(self):

		for t in self.tokens.getTokens():
			self.tlength += math.pow( self.calc_tf( self.get_query_term_length( t ) ) * self.calc_dtf( len( self.index.bank.urls ), t ), 2 )
		self.tlength = math.sqrt( self.tlength )

	def calc_ranking(self):
		for t in self.tokens.getTokens():
			
			it = self.index.getIndexToken( t )
			dtf = self.calc_dtf( len( self.index.bank.urls ), t )

			for d in it.urlList.iterkeys():	
				tf = self.calc_tf( it.urlList[ d ] )
				wtq = tf * dtf

				wtf = self.calc_tf( self.get_query_term_length( t ) )
				wtd = wtf * dtf
				
				if d not in self.ranking:
					self.ranking[ d ] = 0

				self.ranking[ d ] += ( wtq * wtd )

		for d in self.ranking:
			self.ranking[ d ] = self.ranking[ d ] / ( self.lengths[ d ] * self.tlength )

	def calc_tf(self, val):
		return ( 1 + math.log10( val ) )

	def calc_dtf(self, n, token):
		return math.log10( float( n ) / float( self.index.getDocumentFrequency( token ) ) )

	def get_query_term_length(self, token):
		count = 0
		for t in self.tokens.getTokens():
			if t == token:
				count = count + 1
		return count

	def printScoring(self):
		printable = "[";
		for t in self.tokens.getTokens():
			printable += "'%s', " % ( t )
		printable = printable[:-2] + "]\n"
		for item in sorted( self.ranking.items(), key=lambda x: x[1], reverse=True ):
			printable += "%s:\t%.6f\n" % (item[0], item[1] )
		print (printable)

	def printDocumentLength(self):
		printable = "";
		for item in sorted( self.lengths ):
			printable += "%s:\t%.6f\n" % ( item, self.lengths[ item ] )
		print (printable)