from Crawler import Crawler
from Url import Url
from UrlBank import UrlBank
from PageRank import PageRank

def main():

	crawler = Crawler([
		"http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html",
		"http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d06.html",
		"http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d08.html"
	])
	crawler.crawl()
	bank = crawler.getUrlBank()

	#bank.printBank()
	rank = PageRank(bank, 0.95, 0.04)
	rank.calculate()
	rank.bank.printBank()

if __name__ == "__main__":
    main()