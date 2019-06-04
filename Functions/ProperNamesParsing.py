#-*- coding: utf-8 -*-

import csv, json
import time
import urllib
import xml.etree.ElementTree as et


import pandas as pd

# Due to large lag required to receive response it's suggestes to parse titles one-by-one
titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

def properNamesParsing():
    summary=dict()
    properNamesSentList=[]
    with open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\properNamesCategorized.json","r") as properNamesPath:
        properNames=json.load(properNamesPath)
    l ='any2txt|wcrft2({"morfeusz2":true})|wsd|sentiment'
    u = 'IKedracka'
    respDict = dict()

    for title in titles:

        topicSentiment=dict()
        path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\" + title + ".csv"
        file=open(path, 'r')
        data=pd.read_csv(file)
        oldLine=""
        for line in data['Headline']:
            respDict['text'] = line
            respDict['lpmn'] = l
            respDict['user'] = u
            doc = json.dumps(respDict).encode('utf8')
            link = "http://ws.clarin-pl.eu/nlprest2/base/startTask/"
            u = urllib.parse.urlparse(link)
            url = u.geturl()
            base = 'http://ws.clarin-pl.eu/nlprest2/base'
            tid = urllib.request.urlopen(urllib.request.Request(url, data=doc, headers={'Content-Type': 'application/json'})).read().decode('utf8')
            # print(tid)
            time.sleep(0.7)
            resp = json.loads(urllib.request.urlopen(urllib.request.Request(base + '/getStatus/' + tid)).read())
            value = resp['value']
            # print(value)
            if type(value) is not float and type(value) is not int:
                for item in value:
                    content = urllib.request.urlopen(
                        urllib.request.Request(base + '/download' + item['fileID'])).read().decode('utf8')
                    # print(content)
                    root=et.fromstring(content)
                    lemmas=[]
                    sentimentDict=dict()
                    for orth in root.findall('.//orth'):
                        lemmas.append(orth.text)
                    for lemma in lemmas:
                        if lemma.lower() in properNames.keys():
                            # print('Im here')
                            for prop in root.findall('.//prop'):
                                if prop.attrib['key']=='emotion_name':
                                    sentiments=prop.text.split(',')
                                    for sentiment in sentiments:
                                        if sentiment in sentimentDict:
                                            sentimentDict[sentiment]+=1
                                        else:
                                            sentimentDict[sentiment]=1
                            newLine={'Topic':properNames[lemma.lower()],'Media':title,'Sentence':line,'Sentiment':sentimentDict}
                            if newLine['Sentiment'] != {} and newLine['Sentence']!=oldLine:
                                print(orth.text)
                                print(type(newLine))
                                print(newLine)
                                properNamesSentList.append(newLine)
                                oldLine=line
        print(properNamesSentList)
    return properNamesSentList

sentiment=properNamesParsing()
with open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\ResultProperNamesSentiment.csv", "a") as file:
    writer= csv.DictWriter(file, fieldnames=['Topic', 'Media', 'Sentence', 'Sentiment'])
    writer.writerows(sentiment)


