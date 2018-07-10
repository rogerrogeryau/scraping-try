# -*- coding: utf-8 -*-
from time import sleep

from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from selenium.common.exceptions import NoSuchElementException


class BooksSpider(Spider):
    name = 'books'
    start_url = ['books.toscrape.com']

    # def start_requests(self):
    #     self.driver = webdriver.Chrome('/home/roger/scrapy-2/chromedriver')
    #     self.driver.get('http://books.toscrape.com')

    #     sel = Selector(text=self.driver.page_source)
    #     books = sel.xpath('//h3/a/@href').extract()
    #     for book in books:
    #         url = 'http://books.toscrape.com/' + book
    #         yield Request(url, callback=self.parse_book)

        
    #     count = 0

    #     #set stop page
    #     till_page = 3 


    #     while True and count < till_page-1:
    #         try:
    #             next_page = self.driver.find_element_by_xpath('//a[text()="next"]')
    #             sleep(3)
    #             self.logger.info('Sleeping for 3 seconds.')
    #             next_page.click()

    #             sel = Selector(text=self.driver.page_source)
    #             books = sel.xpath('//h3/a/@href').extract()
    #             for book in books:
    #                 url = 'http://books.toscrape.com/catalogue/' + book
    #                 yield Request(url, callback=self.parse_book)

    #         except NoSuchElementException:
    #             self.logger.info('No more pages to load.')
    #             self.driver.quit()
    #             break
            
    #         count+=1

    def parse_book(self, response):
        pass
