from UrlBank 	import UrlBank
from Url 		import Url
from Tokenizer	import Tokenizer

class Scorer():
	def __init__(self):
		pass 

	def calc_tf(self, tokens, term):
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

	def calc_score(self, w_t_q, w_t_d):
		score = (w_t_q * w_t_d) / (math.sqrt(math.pow(w_t_q, 2)) * math.sqrt(math.pow(w_t_d,2)))

	def search_token(self, tokens, term):
		token = 0
		for k in tokens:
			for v in tokens[k]:
				if term in v:
					token = tokens[v]
		return token