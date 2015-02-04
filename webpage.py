from HTMLParser import HTMLParser
import urllib2

f = urllib2.urlopen('https://www.besmith.com/candidates/search?field_state_value=All&field_job_category_tid=&field_job_type_tid=&field_code_value=&body_value=&field_term_tags_value=&page=1&title=')

#titles, URLs, and locations

trstack = []
jobs = []

class IndeedHTMLParser(HTMLParser):
	jobPost = []
	tds = 0
	jobTitle = ""
	
	def handle_starttag(self, tag, attr):
		global trstack
		if tag == 'tr':
			trstack.append('tr')
		if tag == 'td':
			trstack.append('td')
			self.tds = self.tds + 1
		if len(trstack) > 0 and trstack[len(trstack)-1] == 'td' and tag == 'a':
			trstack.append('a')
			self.jobPost.append(str(attr[0][1]))
	def handle_data(self, data):
		global trstack
		if len(trstack) > 0:
			if trstack[len(trstack)-1] == 'a':
				self.jobTitle = self.jobTitle + data
			if trstack[len(trstack)-1] == 'td':
				if self.tds == 4:
					self.jobPost.append(data)
	def handle_endtag(self, tag):
		global trstack
		global jobs
		if len(trstack) > 0:
			if tag == 'td':
				trstack.pop()
			if tag == 'tr':
				trstack.pop()
				self.tds = 0
				jobs.append(self.jobPost)
				self.jobPost = []
			if tag == 'a':
				if len(self.jobTitle) > 0:
					self.jobPost.append(str(self.jobTitle))
					self.jobTitle = ''
				trstack.pop()

parser = IndeedHTMLParser()
parser.feed(f.read())
for job in jobs:
	print job[1].replace(',','') + ',' + 'https://www.besmith.com' + job[0] + ',' + job[2].replace(',','')
