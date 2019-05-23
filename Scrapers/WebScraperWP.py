import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def wp():
    wpHeadlines=dict()
    wp="https://www.wp.pl/"
    page= urllib.request.urlopen(wp)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())

    # news type 1:
    headlines=soup.find_all("div", class_="sc-1bp8799-1 gqsna")
    for headline in headlines:
        # print("WP: " + str(headline.get_text()))
        key=randomStringDigits(8)
        val=str(headline.get_text())
        wpHeadlines[key]=val
    # news type 2:
    headlines2=soup.find_all("div", class_="lclzf3-0 egPcYF")
    for headline in headlines2:
        # print("WP: " + str(headline.get_text()))
        key = randomStringDigits(8)
        val = str(headline.get_text()).strip()
        wpHeadlines[key] = val.strip()
    return wpHeadlines
