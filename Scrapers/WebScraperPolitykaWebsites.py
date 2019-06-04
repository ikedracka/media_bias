#-*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits

def politykaLinks():
    polLinks=[]
    polityka="https://polityka.pl/"
    page= urllib.request.urlopen(polityka)
    soup= bs(page, features="html.parser", from_encoding="utf-8")
    # print(soup.prettify)
    headlines=soup.find_all("a")#, class_="elemRelative") #, class_="driverItemContent")
    for headline in headlines:
        if headline.find("h3") and headline['href'] is not None:
            polLinks.append(headline['href'])
    return polLinks

def politykaTextScraper():
    links=politykaLinks()
    politykaText=[]
    for link in links:
        fullPage=urllib.request.urlopen(link)
        soupLink=bs(fullPage, features="html.parser", from_encoding="utf-8")
        # print(soupLink.prettify())
        ignored=["Ta strona ", "Jesteś już", "Czytaj tak"]
        divs=soupLink.find_all("div", class_="cg_article_content")
        for div in divs:
            ps=div.find_all("p")
            for p in ps:
                if p.text.strip()[:10] not in ignored and p.text.strip()!="":
                    try:
                        line=p.text.replace(u'\xa0', ' ')
                        print(line)
                        politykaText.append(line)
                    except:
                        pass
                    # politykaText.append(line.replace(u'\ufeff',' ').replace(u'\u2b07','').replace(u'\xea','e').replace(u'\xe0','a').replace(u'\u2264',' ').replace(u'\xa5','').replace(u'\xe8','e').replace(u'\u2500', ' ').replace(u'\xe8', 'e').replace(u'\u2032', ' ').replace(u'\xe3', 'a').strip())
    #             print(p.text.replace(u'\u200B', ' ').strip())
    return politykaText
