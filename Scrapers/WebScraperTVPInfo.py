import urllib.request
from bs4 import BeautifulSoup as bs

from Functions.RandomStringDigits import randomStringDigits


def tvpinfo():
    tHeadlines=dict()
    tvp="https://www.tvp.info/"
    page= urllib.request.urlopen(tvp)
    soup = bs(page, features="html.parser")


    # main news:
    mainHeadlines=soup.find_all("h1", class_="title")
    for headline in mainHeadlines:
        # print("TVP Info: " + str(headline.string).strip())
        key=randomStringDigits(8)
        value=str(headline.string).strip()
        tHeadlines[key]=value
    # major news:
    majorNewsHeadlines=soup.find_all("h2", class_="news__title")
    for headline in majorNewsHeadlines:
        # print("TVP Info: " + str(headline.string).strip())
        key = randomStringDigits(8)
        value = str(headline.string).strip()
        tHeadlines[key] = value

    # minor news:
    minorNewsHeadlines=soup.find_all("h3", class_="news__title")
    for headline in minorNewsHeadlines:
        # print("TVP Info: " + str(headline.string).strip())
        key = randomStringDigits(8)
        value = str(headline.string).strip()
        tHeadlines[key] = value

    # info:
    infoHeadlines=soup.find_all("h3", class_="information__text")
    for headline in infoHeadlines:
        # print("TVP Info: " + str(headline.string).strip())
        key = randomStringDigits(8)
        value = str(headline.string).strip()
        tHeadlines[key] = value

    # business:
    businessHeadlines=soup.find_all("h3", class_="business__subtitle")
    for headline in businessHeadlines:
        # print("TVP Info: " + str(headline.string).strip())
        key = randomStringDigits(8)
        value = str(headline.string).strip()
        tHeadlines[key] = value
    return tHeadlines

