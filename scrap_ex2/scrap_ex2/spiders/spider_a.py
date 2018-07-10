# -*- coding: utf-8 -*-
import scrapy

import selenium	
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class SpiderASpider(scrapy.Spider):
    name = 'spider_a'
    allowed_domains = ['books.toscrape.com']

    def start_requests(self):
        self.driver = webdriver.Chrome('/home/roger/scrapy-2/chromedriver')
        self.driver.get('http://books.toscrape.com')

        sel = Selector(text=self.driver.page_source)
        books = sel.xpath('//h3/a/@href').extract()
        for book in books:
            url = 'http://books.toscrape.com/' + book
            yield Request(url, callback=self.parse)


    while True:
        try:
    #         next_page = driver.find_element_by_xpath('//a[text()= "next"]')
    #         sleep(3)
    #         self.logger.info("sleeping for 3 seconds.")
    #         next_page.click()

    #         sel = Selector(text=self.driver.page_source)
    #         books = sel.xpath('//h3/a/@href').extract()
    #         for book in books:
    #             url = 'http://books.toscrape.com/' + book
    #             yield Request(url, callback=self.parse)


    #     except NoSuchElementException:
    #         self.logger.info('No more pags to load.')
    #         self.driver.quit()
    #         break 
        
    def parse(self, response):
        pass
