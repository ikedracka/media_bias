import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def nczas():
    ncHeadlines=dict()
    nczas="https://nczas.com/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req=Request(nczas, headers=hdr)
    page= urlopen(req)
    soup = bs(page, features="html.parser")
    headlines=soup.find_all("h3", class_="entry-title td-module-title")
    for headline in headlines:
        titles=headline.find_all("a")
        for title in titles:
            # print("NCzas: " + str(title['title']))
            key = randomStringDigits(8)
            value = str(title.string)
            ncHeadlines[key] = value
    return ncHeadlines