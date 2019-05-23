import csv
import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def interia():
    iHeadlines=dict()
    interia="https://fakty.interia.pl/"
    page= urllib.request.urlopen(interia)
    soup = bs(page, features="html.parser")
    headlines=soup.find_all("li")
    for headline in headlines:
        magazines=headline.find_all("div", class_="tile-magazine")
        for magazine in magazines:
            headers=magazine.find_all("div", class_="tile-magazine-header")
            for header in headers:
                titles=header.find_all("h2",class_="tile-magazine-title")
                for title in titles:
                    # print("Interia: " + str(title.find("a").string))
                    key = randomStringDigits(8)
                    value = str(title.find("a").string)
                    val=value.replace(u'\u200b','')
                    iHeadlines[key] = val
    return iHeadlines
