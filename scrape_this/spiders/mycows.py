# to test in shell run with 'scrapy shell "<url>"''
# to run the script 'scrapy crawl <name>' without the file extension
# THIS WORKS!!

import scrapy
import re
import csv

class DmozSpider(scrapy.Spider):
    name = "mycows"
    allowed_domains = ["http://www.statesman.com"]
    start_urls = [
        "http://www.statesman.com/staff/"
    ]

    def parse(self, response):
        with open('statemails.csv', 'wb') as csvfile:
            answer = response.xpath('//html/body/div/div/div/div/div/div/div/table/tr/td')
            for sel in answer:
                email = answer.xpath('a/@href').extract()
                emailset = set(email)
                for address in email:
                    if address.startswith('mailto:'):
                        newaddy = re.sub('mailto:', '', address)
                        csvfile.write(str(newaddy + ", "))