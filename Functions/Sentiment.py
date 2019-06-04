#-*- coding: utf-8 -*-

import urllib.parse, json, urllib.request, time, re
import pandas as pd
import xml.etree.ElementTree as et
from Functions.RandomStringDigits import randomStringDigits

# Declaration of titles used in the analysis:
titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

# Declaration of final dataframe that is going to store the results:
headlines=pd.DataFrame(columns=['ID','Title','Sentence','Sentiment'])

def sentimentAnalysis():

    # Initialize dictionary for CLARIN analysis:
    data = dict()
    summary=dict()
    l = 'any2txt|wcrft2({"morfeusz2":true})|wsd|sentiment' # pattern to recognize sentiment analysis
    u = 'IKedracka'
    pattern = re.compile('([^\s\w]|_)+') # regex used remove non-alphanumerical characters

    for title in titles:
        # counter for non-neutral words
        totalNonNeutral=0
        words=list()
        emotions=dict()
        path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataFull\\" + title + ".txt"
        source=open(path,"r")
        words=source.read().split(',')

        # Clearning data - splitting into words and removing non-alphanumerical characters
        text=' '.join(words)
        text=text.replace("'","")
        text=pattern.sub('', text)

        # Test - check if text got parsed correctly:
        # print(text)

        # Declare parameters before passed to CLARIN-PL tool:
        data['text']=text
        data['lpmn']=l
        data['user']=u
        doc=json.dumps(data).encode('utf8')

        # Request response from CLARIN-PL tool after passing headlines dataset
        link="http://ws.clarin-pl.eu/nlprest2/base/startTask/"
        u=urllib.parse.urlparse(link)
        url=u.geturl()
        base='http://ws.clarin-pl.eu/nlprest2/base'
        tid = urllib.request.urlopen(urllib.request.Request(url,data=doc, headers={'Content-Type': 'application/json'})).read().decode('utf8')
        print(tid)

        # WP and WPolityce hold the biggest number of headlines - hence, we need to request longer break between requesting response
        if title in ["WP", "WPolityce"]:
            time.sleep(60)

        # For all other titles, 10s delay is enough
        time.sleep(10)

        # Receiving response
        resp = json.loads(urllib.request.urlopen(urllib.request.Request(base + '/getStatus/' + tid)).read())
        value=resp['value']
        print(value)

        for item in value:
            time.sleep(0.1)
            # Reading response:
            content = urllib.request.urlopen(urllib.request.Request(base + '/download' + item['fileID'])).read().decode('utf8')
            print(title)
            # print(content)
            root=et.fromstring(content)

            # Searching for all elements that contain sentiment analysis for words:
            for tok in root.findall('.//tok'):
                prop=tok.findtext('prop')
                prop=tok.find('prop')
                if prop is not None and prop.attrib['key']=='emotion_name' and len(prop.text) >1:
                    totalNonNeutral+=1
                    sentiment=tok.findtext('prop').split(',')
                    for emotion in sentiment:
                        if emotion in emotions:
                            emotions[emotion]+=1
                        else:
                            emotions[emotion]=1
            emotions['total']=len(words)
            emotions['totalNonNeutral']=totalNonNeutral
            summary[title]=emotions
    return summary

sentiment=sentimentAnalysis()
with open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\resultNaive.json","a") as result:
    json.dump(sentiment, result, ensure_ascii=False)
