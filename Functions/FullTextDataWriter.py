#-*- coding: utf-8 -*-
# Program to consolidate article scrapers and save data for further parsing

# Import webscrapers:
from Scrapers.WebScraperNCzasWebsites import nCzasTextScraper
from Scrapers.WebScraperNewsweekWebsites import newsweekTextScraper
from Scrapers.WebScraperOnetWebsites import onetTextScraper
from Scrapers.WebScraperPolitykaWebsites import politykaTextScraper
from Scrapers.WebScraperWPolityceWebsites import wPolityceTextScraper
import csv

# Declare titles:
titles=['NCzas', 'Newsweek', 'Onet', 'Polityka', 'WPolityce']

# Declare list with news scrapers:
functions=[nCzasTextScraper(), newsweekTextScraper(), onetTextScraper(), politykaTextScraper(), wPolityceTextScraper()]

i=0
for title in titles:
    path="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\ArticleText\\" + title + "Text.txt"
    file= open(path, "w")
    text=functions[i]

    # Check if text parsed correctly:
    # print(text)

    # Write results to the file:
    w=csv.writer(file)
    w.writerow(text)

    # Move to next webscraper on the list
    i+=1