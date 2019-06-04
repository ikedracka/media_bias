#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def onetLinks():
    oLinks=[]
    onet="https://wiadomosci.onet.pl/"
    page= urllib.request.urlopen(onet)
    soup= bs(page, features="html.parser", from_encoding="utf-8")
    # print(soup.prettify)
    headlines=soup.find_all("a") #, class_="driverItemContent")
    for headline in headlines:
        if headline.find("h3") is not None:
                oLinks.append(headline['href'])
    return oLinks

def onetTextScraper():
    onetText=[]
    links=onetLinks()
    for link in links:
        fullPage=urllib.request.urlopen(link)
        soupLink=bs(fullPage, features="html.parser")
        ps=soupLink.find_all("p")
        for p in ps:
            try:
                print(p.text.replace(u'\xa0', ' ').strip())
                onetText.append(p.text.replace(u'\xa0', ' '))
            except:
                pass
            # onetText.append(p.text.replace(u'\u200B', ' ').replace(u'\u2b07','').replace(u'\xea','e').replace(u'\xa5','').replace(u'\xe0','a').replace(u'\xe8','e').strip())
    return onetText
