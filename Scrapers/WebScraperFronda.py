import csv
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from Functions.RandomStringDigits import randomStringDigits


def fronda():
    fHeadlines = dict()
    frondaurl="http://www.fronda.pl/c/wiadomosci,1.html"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = Request(frondaurl, headers=hdr)
    page = urlopen(req)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())
    headlines=soup.find_all("h4")
    for headline in headlines:
        # print("Fronda: " + str(headline.string))
        key = randomStringDigits(8)
        value = str(headline.string)
        fHeadlines[key] = value
    return fHeadlines
