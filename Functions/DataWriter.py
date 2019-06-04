import csv, sched, time, threading
from Scrapers.WebScraperFronda import fronda
from Scrapers.WebScraperGazeta import gazeta
from Scrapers.WebScraperInteria import interia
from Scrapers.WebScraperNCzas import nczas
from Scrapers.WebScraperNewsweek import newsweek
from Scrapers.WebScraperOnet import onet
from Scrapers.WebScraperPolityka import polityka
from Scrapers.WebScraperRMFPolska import rmfpolska
from Scrapers.WebScraperRMFSwiat import rmfswiat
from Scrapers.WebScraperTVN24 import tvn24
from Scrapers.WebScraperTVPInfo import tvpinfo
from Scrapers.WebScraperWP import wp
from Scrapers.WebScraperWPolityce import wpolityce
from Scrapers.WebScraperWprost import wprost
import datetime

titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']
functions=[fronda(),gazeta(), interia(), nczas(),onet(), newsweek(),polityka(),rmfpolska(),rmfswiat(),tvn24(),tvpinfo(),wp(),wpolityce(),wprost()]

def update():
    for i in range(0,len(titles)):
        # Declare data sources and targets
        testString="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataTest\\test"+titles[i]+".csv"
        realString="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\"+titles[i]+".csv"

        # Initialize empty lists to store headlines:
        lastUpdate=[]
        newUpdate=[]

        # Read old data:
        testDataReader=csv.DictReader(open(testString))
        for line in testDataReader:
            lastUpdate.append(str(line['Headline']).strip(u'\u200b'))

        # Read new data:
        newData=functions[i]

        # If new headlines not in old headlines, append new headlines to the file:
        for key, val in newData.items():
            if val not in lastUpdate:
                newUpdate.append(val.replace(u'\u200b','').replace(u'\u2103',' ').replace(u'\u0219','s')) #replacing problematic signs

        # Print recent update:
        print("Update - " + str(titles[i]))
        print(newUpdate)

        # Open file to save with 'append' mode:
        realDataWriter = csv.writer(open(realString, mode="a"))

        # Declare timestamp to append to each line with new headline:
        timestamp=datetime.datetime.now()

        # Save new lines to the file:
        for line in newUpdate:
            line=line.replace(u'\u200b','').replace(u'\u0219','s').replace(u'\u2103',' ')
            realDataWriter.writerow([titles[i],line,timestamp])

        # Save new lines in order to compare with further updates
        testDataWriter=csv.writer(open(testString, mode="w"))
        testDataWriter.writerow(['Title','Headline','Timestamp'])
        for key, val in newData.items():
            value=val.replace(u'\u200b','').replace(u'\u0219','s').replace(u'\u2103',' ')
            testDataWriter.writerow([titles[i],value,timestamp])

    # Print timestamp of function runned:
    frun=datetime.datetime.now()
    print("Function runned: ")
    print(frun)

update()