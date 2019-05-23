import urllib.request
import re
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def tvn24():
    t24Headlines=dict()
    tvn24="https://www.tvn24.pl/"
    page= urllib.request.urlopen(tvn24)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())

    #main news:
    mainHeadlines=soup.find_all("h1")
    for headline in mainHeadlines:
        tags=headline.find_all("a")
        for tag in tags:
            # print("TVN24: " + str(tag.get_text()))
            key = randomStringDigits(8)
            value = tag.get_text()
            t24Headlines[key] = value

    #side news:
    sideHeadlines=soup.find_all("h2")
    for headline in sideHeadlines:
        if headline.has_attr('class'):
            aTag=headline.find("a")
            if aTag is not None:
                if headline['class'][0]=="decorate-heading" and len(str(aTag.string))>30:
                    # print("TVN24: " + str(aTag.string).strip())
                    key = randomStringDigits(8)
                    value = str(aTag.get_text()).strip()
                    t24Headlines[key] = value
    return t24Headlines

