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
    l = 'any2txt|wcrft2|liner2({"model":"top9"})'
    u = 'IKedracka'

    #get text to parse:
    for title in titles:
        words=list()
        emotions=dict()
        path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\" + title + ".csv"
        source=open(path,"r")
        words=pd.read_csv(source, header=0)
        content=words['Headline']
        proper_names=[]
        for headline in content:
            data['text']=headline
            data['lpmn']=l
            data['user']=u
            doc=json.dumps(data).encode('utf8')
            link="http://ws.clarin-pl.eu/nlprest2/base/startTask/"
            u=urllib.parse.urlparse(link)
            url=u.geturl()
            base='http://ws.clarin-pl.eu/nlprest2/base'
            tid = urllib.request.urlopen(urllib.request.Request(url,data=doc, headers={'Content-Type': 'application/json'})).read().decode('utf8')
            # print(tid)
            time.sleep(1)
            resp = json.loads(urllib.request.urlopen(urllib.request.Request(base + '/getStatus/' + tid)).read())
            value=resp['value']
            # print(value)
    #
            for item in value:
                content = urllib.request.urlopen(urllib.request.Request(base + '/download' + item['fileID'])).read().decode('utf8')
                # print(content)
                root=et.fromstring(content)
                # print(root)
                for tok in root.findall('.//tok'):
                    if (tok.findtext('ann') is not None):
                        if int(tok.findtext('ann'))>0:
                            for lex in tok.findall('lex'):
                                base=lex.findtext('base')
                                if base not in proper_names:
                                    proper_names.append(base)
    return proper_names

sentiment=sentimentAnalysis()
with open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\resultProperNames.json","w") as result:
    json.dump(sentiment, result, ensure_ascii=False)