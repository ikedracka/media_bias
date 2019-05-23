# move it to remote and run in the background
# add handling for timeout error for particular websites
import csv, sched, time, threading
from Scrapers.WebScraperDziennik import dziennik
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

titles=['Dziennik','Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']
functions=[dziennik(),fronda(),gazeta(), interia(), nczas(),onet(), newsweek(),polityka(),rmfpolska(),rmfswiat(),tvn24(),tvpinfo(),wp(),wpolityce(),wprost()]

#Gazeta, gazeta()

s=sched.scheduler(time.time, time.sleep)

def update():
    for i in range(0,len(titles)):
        # Declare data sources and targets
        testString="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataTest\\test"+titles[i]+".csv"
        realString="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\"+titles[i]+".csv"

        # Initialize empty lists to store headlines
        lastUpdate=[]
        newUpdate=[]

        # Read old data
        testDataReader=csv.DictReader(open(testString))
        for line in testDataReader:
            lastUpdate.append(str(line['Headline']).strip(u'\u200b'))
        # print("Last Update:")
        # print(lastUpdate)
        newData=functions[i]

        # If new headlines not in old headlines, append new headlines to the file
        for key, val in newData.items():
            if val not in lastUpdate:
                newUpdate.append(val.replace(u'\u200b',''))
        print("Update - " + str(titles[i]))
        print(newUpdate)
        realDataWriter = csv.writer(open(realString, mode="a"))
        timestamp=datetime.datetime.now()
        for line in newUpdate:
            line=line.replace(u'\u200b','')
            realDataWriter.writerow([titles[i],line,timestamp])

        testDataWriter=csv.writer(open(testString, mode="w"))
        testDataWriter.writerow(['Title','Headline','Timestamp'])
        for key, val in newData.items():
            value=val.replace(u'\u200b','')
            testDataWriter.writerow([titles[i],value,timestamp])
        frun=datetime.datetime.now()
    print("Function runned: ")
    print(frun)

def run():
    threading.Timer(600,run).start()
    update()

# run()
#
update()