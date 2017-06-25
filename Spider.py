import scrapy




class nerdSpider(scrapy.spider):
	name = "Nerdy Spider"
	
	def start_requests(self):
	
		urls = ['https://crackerbarrel.com']
		for url in urls:
			yield scrapy.Request(url = url, callback=self.parse)
			
	def parse(self, response):
		
		page = self.url.split("/")[-2]
		filename = 'quotes-%s.html' % page
		for i in response.css('body::text')
			with open(filename, 'wb') as f:
				f.write(i+'\n')
		self.log('Saved file %s' % filename)
		
