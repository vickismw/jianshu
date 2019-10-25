# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from selenium import webdriver
from scrapy.http.response.html import HtmlResponse

class JianshuDownloaderMiddleware(object):

    def __init__(self):
        # 加载测试浏览器
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")

    # request: 则scrapy框架会去服务器加载资源
    # reponse: 则跳过资源下载直接交给解析器方法
    def process_request(self, request, spider):
        # 模拟人类访问页面的行为,并且单击收入的专题按钮(按钮存在的话)
        self.driver.get(request.url)
        # 为了防止页面加载过慢,则等待1秒
        time.sleep(1)
        # 目前页面已经在测试浏览器中
        try:
            while True:
                show_more = self.driver.find_element_by_class_name('show-more')
                show_more.click()
                print('-'*100)
                time.sleep(0.5)
        except:
            print('别在单击了，已经没有了')
        source = self.driver.page_source
        # 创建一个response对象,把页面信息都封装在reponse对象中
        response = HtmlResponse(url=self.driver.current_url,body=source,request = request,encoding="utf-8")
        return response