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

	bank = crawler.get_bank()
	bank.sortBank()

	print '\nLinkstruktur: \n' 
	bank.printOutgoing()

	print '\nPageRanks:'
	rank = PageRank(bank, 0.95, 0.04)
	rank.calculate()

	print '\n\nIndex: \n'
	i = Index( bank )
	i.printIndex()

	s = Scorer( 'tokens', i )
	
	print '\nDokumentenlaenge: \n'
	s.printDocumentLength()
	
	print '\nSuchergebnisse: \n'
	s.printScoring()
	s = Scorer( 'index', i )
	s.printScoring()
	s = Scorer( 'classification', i )
	s.printScoring()
	s = Scorer( 'tokens classification', i )
	s.printScoring()

if __name__ == "__main__":
    main()
