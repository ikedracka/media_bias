
import urllib.request
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
from Functions.RandomStringDigits import randomStringDigits

def dziennik():
    dHeadlines=dict()
    dziennik="https://wiadomosci.dziennik.pl/"
    page= urllib.request.urlopen(dziennik)
    soup = bs(page, features="html.parser")
    # print(soup.prettify())
    headlines=soup.find_all("span")
    for headline in headlines:
        texts=headline.find_all("a")
        for text in texts:
            if len(text['title'])>20:
                # print("Dziennik: " + str(text["title"]))
                key=randomStringDigits(8)
                value=str(text["title"])
                dHeadlines[key]=value
    return dHeadlines

# print(dziennik())