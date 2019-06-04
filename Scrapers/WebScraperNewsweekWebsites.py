#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits

def newsweekLinks():
    nLinks=[]
    onet="https://newsweek.pl/"
    page= urllib.request.urlopen(onet)
    soup= bs(page, features="html.parser", from_encoding="utf-8")
    # print(soup.prettify)
    headlines=soup.find_all("a", class_="elemRelative") #, class_="driverItemContent")
    for headline in headlines:
        if headline['href'] is not None:
            nLinks.append(headline['href'])
    return nLinks

def newsweekTextScraper():
    links=newsweekLinks()
    newsweekText=[]
    for link in links:
        fullPage=urllib.request.urlopen(link)
        soupLink=bs(fullPage, features="html.parser")
        # print(soupLink.prettify())
        ps=soupLink.find_all("p")
        for p in ps:
            try:
                print(p.text.strip())
                newsweekText.append(p.text.strip())
            except:
                pass
            # newsweekText.append(p.text.replace(u'\u200B', ' ').replace(u'\u2b07','').replace(u'\xea','e').replace(u'\xa5', '').replace(u'\xe8','e').replace(u'\xe0','a').strip())
    return newsweekText
