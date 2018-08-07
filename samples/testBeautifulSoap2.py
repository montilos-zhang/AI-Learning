# -*- coding:utf-8 -*-
import urllib
import os, datetime, sys
from bs4 import BeautifulSoup
#reload(sys)
sys.setdefaultencoding( "utf-8" )
sys.setswitchinterval(2)
__BASEURL__ = "http://bj.58.com/"
__INITURL__ = "http://bj.58.com/hezu/"
soup=BeautifulSoup(urllib.urlopen(__INITURL__))
lv1Elements = soup.html.body.section.find('div', 'relative').find('dl', 'secitem')('a',href=True)
f=open('data.txt', 'w')
for element in lv1Elements[1:]:
  f.write((element.get_text() + '\r\n'))
  print(element.get_text())
  url = __BASEURL__ + element.get('href')
  print(url)
  soup=BeautifulSoup(urllib.urlopen(url))
  lv2Elements = soup.html.body.section.find('div', 'relative').find('dl', 'secitem').find('div', 'subarea').find_all('a')
  texts = [t.get_text() for t in lv2Elements]
  f.write(' '.join(texts) + '\r\n\r\n')
f.close()