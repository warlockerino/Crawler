<<<<<<< HEAD
from Url 		import Url
from UrlBank 	import UrlBank

class UrlStuff():	
	def main():
	    
	    u1 = Url("reddit.com", ["google.de", "xkcd.com", "google.de"], "random html")
	    u2 = Url("oracle.com", ["reddit.com","google.de","xkcd.com"], "rand html")
	    u3 = Url("google.de", ["reddit.com","reddit.com", "oracle.com"], "some html created in Django")
	    u4 = Url("xkcd.com", ["reddit.com"], "some very simple html")

	    ub = UrlBank()
	    
	    ub.addUrl(u1)
	    ub.addUrl(u2)
	    ub.addUrl(u3)
	    ub.addUrl(u4)

	    ub.printBank()

	if  __name__ =='__main__':main()
=======
import crawler

crawl = crawler.Crawler("http://people.f4.htw-berlin.de/fileadmin/user_upload/Dozenten/WI-Dozenten/Classen/DAWeb/smdocs/d01.html")

crawl.crawl()
>>>>>>> 6e30af1bfe7a624d94ca2528da2822a5a2743d1a
