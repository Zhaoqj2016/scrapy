
# -*- coding:utf-8 -*-
#!C:/Python27
import urllib
import urllib2
import time
import random
import string
import re
from _ast import Param
from selenium import webdriver
class  test: 
    
    def test1(self,parm):
        page = 0
        url = 'http://chuansong.me/account/shiji5000?start=' + str(page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        request = urllib2.Request(url,headers=headers) 
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        pattern = re.compile(r'<span style="float: right;font-weight: normal"><a style="color: #999" href="#;"(.*?)&amp;.*?</span>', re.S)
        print 123
        items = re.findall(pattern,content)
        for item in items: 
            strlist = item.split('url=')
            print item
            print strlist[1]
            self.test2(strlist[1])
                
                   
           
            
    def test2(self,parm):
        url = parm
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        try:
            driver = webdriver.PhantomJS(executable_path='C:\\Python27\\Scripts\\phantomjs') 
            driver.get(url)
            data =  driver.find_element_by_id('page-content').text
            data2=  driver.find_element_by_id('activity-name').text
            print data
            driver.quit
            inpath = 'F:/3.0/Asynonyms/微信文章'+random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')+'.txt'
            uipath = unicode(inpath, "utf8")
            f=open(uipath,'a')
            f.write('【'+data2.encode('utf-8')+'】'+'\n'+data.encode('utf-8'))    
            f.close() 
        except:EOFError           
spider = test()
spider.test1(0)