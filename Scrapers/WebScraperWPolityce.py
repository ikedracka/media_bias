import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def wpolityce():
    wpolHeadlines=dict()
    wpolityce="https://wpolityce.pl"
    page= urllib.request.urlopen(wpolityce)
    soup = bs(page, features="html.parser")
    headlines=soup.find_all("span", class_="long-title")
    for headline in headlines:
        # print("WPolityce: " + str(headline.string))
        key=randomStringDigits(8)
        val=str(headline.string)
        wpolHeadlines[key]=val
    return wpolHeadlines
