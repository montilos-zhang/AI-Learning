

from bs4 import BeautifulSoup as bs
import requests

headers = {
  "host": "www.jd.com",
  "User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/47.0.2526.80 Safari/537.36 Core/1.47.933.400 ",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
  }
session = requests.session()

def get_url():
  renspned = bs(session.get('http://www.jd.com/',headers = headers).text,'html.parser')
  print(renspned.name)
  print(renspned.head.name)
  print(renspned.title)
  dd_inner = renspned.find("div",{"class": "service_entry"})

  #print(renspned.find("div",{"class": "service_entry"}))
  if(dd_inner is not None):
    for i in dd_inner.find_all("span",{"class":"service_txt"}):
      print(i.get_text())

get_url()