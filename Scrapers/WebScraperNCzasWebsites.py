#-*- coding: utf-8 -*-

import re, sys
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits

def nCzasLinks():
    nCzLinks=[]
    nczas = "https://nczas.com/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(nczas, headers=hdr)
    page= urlopen(req)
    soup= bs(page, features="html.parser", from_encoding="utf-8")
    # print(soup.prettify)
    headlines=soup.find_all("a", class_="td-image-wrap")#, class_="elemRelative") #, class_="driverItemContent")
    for headline in headlines:
        if headline['href'] is not None:
            nCzLinks.append(headline['href'])
    return nCzLinks
#
def nCzasTextScraper():
    nCzasText=[]
    links=nCzasLinks()
    for link in links:
        regex = '/ [\\u{1f600}-\\u{1f64f}] /'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(link, headers=hdr)
        fullPage = urlopen(req)
        soupLink=bs(fullPage, features="html.parser")
        # print(soupLink.prettify())
        ignored = ["Źródło"]
        divs=soupLink.find_all("div", class_="td-post-content")
        for div in divs:
            ps=div.find_all("p", class_=None)
            for p in ps:
                if p.text[:6] not in ignored:
                    try:
                        print(p.text)
                        nCzasText.append(p.text)
                    except:
                        pass
    return nCzasText
        # for p in ps:
        #     if len(p.text)>200 and p.text[:5] not in ignored:
        #         print(re.sub('(youtu.be)\/([A-Za-z0-9\-])\w+','',p.text.replace(u'\ufeff', ' ')))
        #     # print(p.text.replace(u'\u200B', ' ').strip())
# U+1F3F3, U+FE0F, U+200D, U+1F308
