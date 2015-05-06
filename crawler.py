from bs4 import BeautifulSoup
import urllib2, httplib, urlparse

from Url import Url
from UrlBank import UrlBank


class Crawler:
	def __init__(self, init_urls):
		self.bank = UrlBank()		

		for init in init_urls:
			self.bank.add(init)			

	def crawl(self):
		while len(self.bank.toCrawl) > self.bank.counter:
			url = self.bank.next()			
			self.visit_url(url)

	def visit_url(self, url):
		request = urllib2.Request(url)

		try:
			response = urllib2.urlopen(request, None, 10)
		except (urllib2.HTTPError, httplib.BadStatusLine) as e:
			print e

		if response != None:	
			typ = response.read()
			outLinks = self.extract_outgoing_links(typ, url)
			page = Url(url, outLinks, self.extract_text(typ))
			
			for out in outLinks:
				self.bank.add(out)

			self.bank.addUrl(page)
	#
	def extract_outgoing_links(self, html, url):
		soup = BeautifulSoup(html)
		links = []
	
		for link in soup.findAll('a'):
			links.append(urlparse.urljoin(url, link.get('href')))

		return links

	#
	def extract_text(self, html):
		soup = BeautifulSoup(html)
		text = soup.get_text()
		
		return text

	#
	def get_bank(self):
		return self.bank

