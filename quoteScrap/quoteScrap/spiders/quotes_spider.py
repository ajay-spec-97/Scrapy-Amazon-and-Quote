# -*- coding: utf-8 -*-

import scrapy
from ..items import QuotescrapItem         

class QuoteSpider(scrapy.Spider):                    # This class we inherit from Spider from Scrapy class(includes inbuilt methods)
    name = 'quote'                                   # name of the spider
    page_number = 2
    
    start_urls = [                                   # list of urls to scrap 
        'http://quotes.toscrape.com/page/1/'         #we start by page 1
        ]
    
    def parse(self, response):                          # response variable contains source code of the website we are scrapping
        items = QuotescrapItem()                        #item is object of class imported Quotescrapitem()
        
        all_div_quotes = response.css('div.quote')      # from source code(response) we extract all tags from class_name "quote"
        
        for quote in all_div_quotes:                             # iterate all the quote from all_div_quotes for 1 page
            title = quote.css('span.text::text').extract()       # extract only "text" from class span with name = "text"
            author = quote.css('small.author::text').extract()   # extract only "text" from class small with name = "author"
            tag = quote.css('.tag::text').extract()              #extract tag    
            
            items['title'] = title                              # title var from spider is assigned to..[] bracket variable used is from items.py file
            items['author'] = author
            items['tag'] = tag
            
            yield items                                             #yield items are sent to pipeline
            
        next_page = 'http://quotes.toscrape.com/page/'+str(QuoteSpider.page_number)+'/'        #value of page_number for next page scraping in the same url # str() to convert integer back to string
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1                        # increment page_number by 1
            yield response.follow(next_page, callback=self.parse) #if next_page has value follow() will take us to next page and callback parse()
            
            
            '''
            yield {                         # we are extracting values in form of dictionary,# we use yield instead of return keyword in spider
                'title' : title,
                'author' : author,
                'tag' : tag
                }
            '''