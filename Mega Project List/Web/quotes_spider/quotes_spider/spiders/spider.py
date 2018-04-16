# Created April 15th, 2018
# This program really only runs once. Run it once, it'll save all the quotes in a text file
# Every time I start the terminal, a random quote appears.
# This makes it faster than running the script everytime to get a random quote
# I use shuf to randomly chose a line (With .bashrc)

import scrapy
import random as rand # To pick a random quote from quotes list

class quotes_spider(scrapy.Spider):
	name = "quotes"
	start_urls = [
		"http://wisdomquotes.com/life-quotes/",
	]

	def parse(self, response):
		quotes = []
		# random_quote = ""

		with open("quote.txt", "w") as quote_file:
			for quote in response.xpath("//blockquote/p").extract():
				# Basically, I don't want to deal with links as a beginner
				# They are a pain in the ass
				if "<a" in quote:
					continue
				else: 
					# Removes the <p> and </p>
					quote = quote[3:-4]
					quote_file.write(quote + '\n')

		#random_quote = "Daily quote: " + quotes[rand.randint(0, len(quotes)-1)]
		#print(random_quote)
