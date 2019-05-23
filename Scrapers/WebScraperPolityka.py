import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def polityka():
    pHeadlines=dict()
    polityka="https://www.polityka.pl/TygodnikPolityka"
    page= urllib.request.urlopen(polityka)
    soup = bs(page, features="html.parser")

    # side headlines
    sideHeadlines=soup.find_all("h3")
    for headline in sideHeadlines:
        if headline.string is not None:
            # print("Polityka: " + str(headline.string).strip())
            key = randomStringDigits(8)
            value = str(headline.string).strip()
            pHeadlines[key] = value
    return pHeadlines
