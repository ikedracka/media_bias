import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def rmfpolska():
    rpHeadlines=dict()
    rmfPoland="https://www.rmf24.pl/fakty/polska"
    page= urllib.request.urlopen(rmfPoland)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())
    headlines=soup.find_all("div", class_="boxBody")
    for headline in headlines:
        imgs=headline.find_all("img")
        for img in imgs:
            # print("RMF Polska: " + str(img['alt']))
            key = randomStringDigits(8)
            value = str(img['alt']).strip()
            rpHeadlines[key] = value
    return rpHeadlines
