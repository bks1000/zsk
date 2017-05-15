# coding:utf-8

import re
import json
import csdnzsk.items
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector 
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.contrib.linkextractors import LinkExtractor

# csdn 知识库
class Zsk(CrawlSpider):
    name = "zsk"
    allowed_domains = ["csdn.net"]
    start_urls = [
        "http://lib.csdn.net"
    ]
    rules = [ # 定义爬取URL的规则
        # (没有callback意味着follow默认为True)
        #Rule(LinkExtractor(allow=('/base/\w+'),deny=('/base/\w+/resource/\w+'))),

        Rule(sle(allow=("/bases/\w+")), follow=True, callback='parse_item'),
        Rule(sle(allow=("/base/\w+")), follow=False, callback='parse_item')
    ]
    
    
    def parse_item(self,response):
        #print response.url
        #logtxt = open("F:\\HW\\scrapyzsk\\csdnzsk\\zsk.txt",'a+')
        #logtxt.write(response.url+'\r\n')
        #logtxt.close()
        try:
            hxs = HtmlXPathSelector(response)
            item = csdnzsk.items.CsdnzskItem()
            item['name']=hxs.select("//div[@class='banner_log']/em/text()")[0].extract()
            item['url']=response.url
            print """**********%s\r\n""" % response.url
            return item
        except Exception,e:
            print Exception,":",e