# -*- coding: utf-8 -*-

import scrapy
from ..items import AmazonscrapItem

class QuoteSpider(scrapy.Spider):                    # This class we inherit from Spider from Scrapy class(includes inbuilt methods)
    name = 'amazon'                                   # name of the spider
    page_number = 2
    
    start_urls = [                                                 # list of urls to scrap 
        'https://www.amazon.com/s?k=gaming+laptops&ref=nb_sb_noss_1'
        ]
    
    def parse(self, response):                          # response variable contains source code of the website we are scrapping
        items = AmazonscrapItem()
        
        product_name = response.css('.a-size-medium::text').extract()
        product_price = response.css('.a-price-whole::text').extract()
        product_imagelink = response.css('.s-image-fixed-height .s-image::attr(src)').extract()   #getting img link from attribute "src"
        
        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
        
        next_page = 'https://www.amazon.com/s?k=gaming+laptop&page='+str(QuoteSpider.page_number)+'&qid=1587299143&swrs=3B0FC09B84242442642FEF2CD0D7AAEB&ref=sr_pg_2'
        if QuoteSpider.page_number <= 20:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)           #follow method will loop every page with parse() method