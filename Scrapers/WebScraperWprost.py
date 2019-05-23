import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def wprost():
    wprHeadlines=dict()
    wprost = "https://www.wprost.pl/wiadomosci"
    page= urllib.request.urlopen(wprost)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())
    headlines=soup.find_all("span")
    for headline in headlines:
        if headline.string is not None:
            if len(str(headline.string))>30:
                key=randomStringDigits(8)
                val=str(headline.string).replace(u'\xa0',' ')
                wprHeadlines[key]=val
    return wprHeadlines

# print(wprost())