#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import json

titles=['Fronda', 'Gazeta', 'NCzas', 'Newsweek', 'Onet', 'Polityka', 'WPolityce']

path="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\ResultProperNamesSentiment.csv"
file=open(path,'r')
sentDF=pd.read_csv(file)
# print(sentDF)
topics=sentDF['Topic']
# print(topics)
topicList=[]
summary=[]
# print(topicList)
countRows=dict()
cleanedRows=dict()

for index, row in sentDF.iterrows():
    if row['Topic'] not in countRows.keys():
        countRows[row['Topic']]=1
    else:
        countRows[row['Topic']]+=1

for key, value in countRows.items():
    if int(countRows[key])>10:
        print(key, value)
        cleanedRows[key]=value

topicList=['pis', 'koalicja obywatelska', 'wiosna', 'konfederacja', 'kościół']
fullDict=dict()
for title in titles:
    partialDict=dict()
    content=sentDF.loc[sentDF['Media']==title]
    for topic in topicList:
        sentList=dict()
        t=content.loc[content['Topic']==topic]
        for index, row in t.iterrows():
            row['Sentiment']=row['Sentiment'].replace("'",'"')
            sentiment=json.loads(row['Sentiment'])
            for key, value in sentiment.items():
                if key in sentList.keys():
                    sentList[key]+=1
                else:
                    sentList[key]=1
        partialDict[topic]=sentList
    fullDict[title]=partialDict

for key, value in fullDict.items():
    print(key, value)

emotions = ['smutek', 'strach', 'złość', 'wstręt', 'zaskoczenie czymś nieprzewidywanym', 'radość', 'zaufanie', 'cieszenie się na coś oczekiwanego']

for topic in topicList:
    globalMax=0
    fig=plt.figure()
    order=1
    for title in titles:
        sentDataset=fullDict[title][topic]
        for emotion in emotions:
            if emotion in sentDataset.keys():
                if sentDataset[emotion]>globalMax:
                    globalMax=sentDataset[emotion]

    for title in titles:
        max=0
        data=dict()
        sentDataset=fullDict[title][topic]
        for emotion in emotions:
            if emotion not in data.keys():
                if emotion in sentDataset.keys():
                    # print(sentDataset[emotion])
                    data[emotion]=sentDataset[emotion]
                else:
                    data[emotion]=0
        x=[]
        y=[]
        for key, value in data.items():
            print(topic, title, key, value)
            if key=='zaskoczenie czymś nieprzewidywanym':
                key='z.cz.n'
                x.append(key)
            elif key=='cieszenie się na coś oczekiwanego':
                key='c.s.n.c.o.'
                x.append(key)
            else:
                x.append(key)
            y.append(value)
        plot=fig.add_subplot(4,2,order)
        plot.barh(x,y,color=['r','r','r','r','r','g','g','g'])
        plot.set_xlim([0,globalMax])
        plt.title(title, fontsize=8)
        order+=1
    plt.suptitle(topic)
    plt.show()