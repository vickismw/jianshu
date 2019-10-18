# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import etree
from douban.items import DoubanItem

class JianshuSpiderSpider(CrawlSpider):
    name = 'jianshu_spider'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    # 可以指定爬虫抓取的规则，支持正则表达式
    # https://www.jianshu.com/p/df7cad4eb8d8
    # https://www.jianshu.com/p/07b0456cbadb?*****
    # https://www.jianshu.com/p/.*
    rules = (
        Rule(LinkExtractor(allow=r'https://www.jianshu.com/p/[0-9a-z]{12}.*'), callback='parse_item', follow=True),
    )
    # name = title = url = collection = scrapy.Field()
    def parse_item(self, response):
        html =etree.HTML(response.text)
        item = DoubanItem()
        item['title'] = html.xpath("//title/text()")[0].split("-")[0]
        item['name'] = html.xpath("//span[@class='name']/a/text()")[0]
        item['url'] = response.url.split("?")[0]
        collection = html.xpath("//div[@class='include-collection']/a/div[@class='name']/text()")
        if collection:
            item['collection'] = ','.join(collection)
        yield item

