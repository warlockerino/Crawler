from bs4 import BeautifulSoup
from Url import Url
from UrlBank import UrlBank
import urllib2, httplib, urlparse
import time
 
import frontier
 
class Crawler(object):
	def __init__(self, init_urls):
		self.frontier = frontier.Frontier()
		for init in init_urls:
			self.frontier.add(init)
		self.bank = UrlBank()
 
	def crawl(self):
		while len(self.frontier) > 0:
			next_time, next_url = self.frontier.next()
 
			while time.time() < next_time:
				time.sleep(0.5)
 
			try:
				self.visit_url(next_url)
			
			except urllib2.URLError:
				continue
 
	def visit_url(self, url):
		print("Visiting URL: %s" % url)
		self.frontier.notify_visit(url)
		request = urllib2.Request(url)
 
		try:
			response = urllib2.urlopen(request, None, 10)
		except (urllib2.HTTPError, httplib.BadStatusLine) as e:
			print e
 
		if response != None:
			self.new_urls(url, response.read())
 
	def new_urls(self, url, html):
		print("Fetching new URLs from: %s" % url)
		outGoingLinks = []
		try:
			for page in self.extract_urls(html):
				page = urlparse.urljoin(url, page)
				#add ougoing links
				outGoingLinks.append(page)
				self.frontier.add(page)
			# add url
			u = Url(url, outGoingLinks, html)
			self.bank.addUrl(u)
		except UnicodeEncodeError:
			pass
 
	def extract_urls(self, page):
		soup = BeautifulSoup(page)
		return [link.get('href') for link in soup.findAll('a')]

	def getUrlBank(self):
		return self.bank
