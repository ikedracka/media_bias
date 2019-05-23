import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def rmfswiat():
    rsHeadlines=dict()
    rmfWorld="https://www.rmf24.pl/fakty/swiat"
    page= urllib.request.urlopen(rmfWorld)
    soup = bs(page, features="html.parser")
    headlines=soup.find_all("div", class_="boxBody")
    for headline in headlines:
        imgs=headline.find_all("img")
        for img in imgs:
            key = randomStringDigits(8)
            value = str(img['alt']).strip().replace(u'\u200b','')
            rsHeadlines[key] = value
    return rsHeadlines

# print(rmfswiat())
