
#-*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits

def wPolityceLinks():
    wpLinks=[]
    wPolityce="https://wpolityce.pl/"
    page= urllib.request.urlopen(wPolityce)
    soup= bs(page, features="html.parser")
    # print(soup.encode('utf-8'))
    headlines=soup.find_all("a", class_="nu-widget-article-list__link")#, class_="elemRelative") #, class_="driverItemContent")
    for headline in headlines:
        # print(headline)
        if headline['href'] is not None:
            # print(headline['href'])
            page="https://wpolityce.pl"+headline['href']
            wpLinks.append(page)
    return wpLinks
#
def wPolityceTextScraper():
    links=wPolityceLinks()
    wPolityceText=[]
    for link in links:
        fullPage=urllib.request.urlopen(link)
        soupLink=bs(fullPage, features="html.parser")
        # print(soupLink.prettify())
        ps=soupLink.find_all("p")
        ignored=["Zespół:", "Autorzy"]
        for p in ps:
            if len(p.text)>200 and p.text[:7] not in ignored:
                try:
                    line=p.text.replace(u'\xa0', ' ')
                    print(line)
                    wPolityceText.append(line)
                except:
                    pass
                # wPolityceText.append((p.text.replace(u'\u200B', ' ').replace(u'\u2b07','').replace(u'\xea','e').replace(u'\xe0','a').replace(u'\xa5','').replace(u'\xe8','e').strip()))
    return wPolityceText
