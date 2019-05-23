import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def onet():
    oHeadlines=dict()
    onet="https://wiadomosci.onet.pl/"
    page= urllib.request.urlopen(onet)
    soup= bs(page, features="html.parser")
    headlines=soup.find_all("h3")
    for headline in headlines:
        # print("Onet: " + str(headline.string))
        key = randomStringDigits(8)
        value = str(headline.string)
        oHeadlines[key] = value
    return oHeadlines
