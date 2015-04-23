from bs4 import BeautifulSoup
import urllib2, httplib, urlparse
import time
 
import frontier
 
class Crawler(object):
	def __init__(self, init_url):
		self.frontier = frontier.Frontier()
		self.frontier.add(init_url)
 
	def polite_time(self):
		return self.frontier.polite_time
 
	def polite_time(self, seconds):
		if seconds >= 0:
			self.frontier.polite_time = seconds
 
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
 
		try:
			for page in self.extract_urls(html):
				page = urlparse.urljoin(url, page)
				self.frontier.add(page)
		except UnicodeEncodeError:
			pass
 
	def extract_urls(self, page):
		soup = BeautifulSoup(page)
		return [link.get('href') for link in soup.findAll('a')]
