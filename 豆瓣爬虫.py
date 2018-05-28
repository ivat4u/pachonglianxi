# -*- coding:utf-8 -*-
import bs4
import re
import urllib2
import urllib
from bs4 import BeautifulSoup
import pandas as pd

url='https://book.douban.com/tag/%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent': user_agent}
data = urllib.urlencode(headers,'utf-8')
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
page = response.read()
soup = BeautifulSoup(page,'lxml')


a=soup.find_all(onclick=re.compile("moreurl.*"))
names=[]
for child in a:
    if child.has_attr('title'):
     name=child['title']
     names.append(name)

'''for i in names:
    print i+'\n'''
date=[]
a=soup.find_all(class_=re.compile("pub"))
for i in a:
     date.append(i.text)

a = soup.find_all(class_=re.compile("star clearfix"))
star=[]
for i in a:
     star.append(i.text)

a=soup.find_all("li", class_="subject-item")
info=[]
for child in a:
    a3=child.contents[3]
    if a3.p!=None:
        info.append(a3.p.text)
    else:
        info.append("")

data=pd.DataFrame()
data.insert(0,"name",names)
data.insert(1,"date",date)
data.insert(2,"stra",star)
data.insert(3,"info",info)

data.to_csv('douban.csv',encoding='utf-8')
