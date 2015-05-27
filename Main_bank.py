from crawler 	import Crawler
from Url 		import Url
from UrlBank 	import UrlBank
from PageRank 	import PageRank
from Tokenizer 	import Tokenizer
from Index 		import Index
from Scorer 	import Scorer

def main():

	crawler = Crawler([
		"http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
		"http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
		"http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html"
	])
	crawler.crawl()

	s  = Scorer()
	bank = crawler.get_bank()

	bank.sortBank()

	print 'Page Ranks: \n'
	rank = PageRank(bank, 0.95, 0.04)
	rank.calculate()

	print '\nIndex: \n'
	i = Index( bank )
	i.printIndex()

	print '\nLinkstruktur: \n' 
#	rank.bank.printBank()

	bank.printOutgoing()
#	t 	= Tokenizer()

#	duh = t.tokenize("Hi there! Whats up Hi")
#	print "DUH:"
#	print duh
#	duh_2 = t.sortTokens(duh)
#	print "---------"
#	print duh_2


if __name__ == "__main__":
    main()
