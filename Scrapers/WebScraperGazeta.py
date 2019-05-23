import csv
import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def gazeta():
    gHeadlines=dict()
    gazeta="http://wiadomosci.gazeta.pl/wiadomosci/0,0.html"
    page= urllib.request.urlopen(gazeta)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())
    headlines=soup.find_all("li", class_="entry")
    for headline in headlines:
        titles=headline.find_all("a")
        for title in titles:
            if title.string is not None:
                # print("Gazeta: " + str(title.string))
                key = randomStringDigits(8)
                value = str(title.string)
                gHeadlines[key] = value
    return gHeadlines

# print(gazeta())
