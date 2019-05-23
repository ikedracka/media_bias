import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def newsweek():
    nHeadlines=dict()
    newsweek="https://www.newsweek.pl/"
    page= urllib.request.urlopen(newsweek)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())

    headlines=soup.find_all("h2", class_="artTitle")
    for headline in headlines:
        if headline.string is not None:
            key = randomStringDigits(8)
            value = str(headline.string)
            nHeadlines[key] = value
    return nHeadlines

