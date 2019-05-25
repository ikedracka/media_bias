#-*- coding: utf-8 -*-
# get all files containing real data
# parse into pandas DataFrames
# For each sentence create line in dict: Origin, sentence, dict with number of words of certain emotions

import urllib.parse, json, urllib.request, time, csv
import pandas as pd
import xml.etree.ElementTree as et
from Functions.RandomStringDigits import randomStringDigits

# declare titles
#Dziennik, Fronda
titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

# declare final dataframe with sentiments
headlines=pd.DataFrame(columns=['ID','Title','Sentence','Sentiment'])



def sentimentAnalysis(): #source as path to csv file
    # initialize dictionary for CLARIN analysis:
    data = dict()
    summary=dict()
    l = 'any2txt|wcrft2({"morfeusz2":true})|wsd|sentiment'
    u = 'IKedracka'

    #get text to parse:
    for title in titles:
        words=list()
        emotions=dict()
        path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataFull\\" + title + ".txt"
        source=open(path,"r")
        words=source.read().split(',')
        text=' '.join(words)
        text=text.replace("'","")
        print(text)
        data['text']=text
        data['lpmn']=l
        data['user']=u
        doc=json.dumps(data).encode('utf8')
        link="http://ws.clarin-pl.eu/nlprest2/base/startTask/"
        u=urllib.parse.urlparse(link)
        url=u.geturl()
        base='http://ws.clarin-pl.eu/nlprest2/base'
        tid = urllib.request.urlopen(urllib.request.Request(url,data=doc, headers={'Content-Type': 'application/json'})).read().decode('utf8')
        print(tid)
        time.sleep(20)
        resp = json.loads(urllib.request.urlopen(urllib.request.Request(base + '/getStatus/' + tid)).read())
        value=resp['value']
        print(value)

        for item in value:
            content = urllib.request.urlopen(urllib.request.Request(base + '/download' + item['fileID'])).read().decode('utf8')
            # print(content)
            root=et.fromstring(content)
            for tok in root.findall('.//tok'):
                if tok.findtext('prop') is not None and len(tok.findtext('prop')) >1:
                    # print(tok.findtext('orth'))
                    # print(tok.findtext('prop'))
                    sentiment=tok.findtext('prop').split(',')
                    for emotion in sentiment:
                        if emotion in emotions:
                            emotions[emotion]+=1
                        else:
                            emotions[emotion]=1
            summary[title]=emotions
    return summary

sentiment=sentimentAnalysis()
with open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\resultNaive.json","w") as result:
    json.dump(sentiment, result, ensure_ascii=False)
