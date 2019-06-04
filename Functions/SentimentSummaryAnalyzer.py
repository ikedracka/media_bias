#-*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt
import numpy as np

file=open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\resultNaive.json")
reader=json.load(file)
fullTitleList=[['Fronda','Gazeta','Interia','NCzas'],['Newsweek','Onet','Polityka','RMFPolska'],['RMFSwiat','TVN24','TVPInfo','WP'],['WPolityce','Wprost']]



for titles in fullTitleList:
    fig=plt.figure()
    order = 1
    for title in titles:
        keys=['smutek', 'strach', 'złość','wstręt', 'zaskoczenie czymś nieprzewidywanym','radość','zaufanie', 'cieszenie się na coś oczekiwanego']
        data=reader[title]
        values=[]
        positiveKeys=['radość', 'zaufanie', 'cieszenie się na coś oczekiwanego']
        total=0
        positive=0
        negative=0
        for key in keys:
            total+=data[key]

        for key in keys:
            if key in positiveKeys:
                positive+=data[key]
            else:
                negative+=data[key]

        for key in keys:
            values.append(data[key]/total)

        for n, i in enumerate(keys):
            if i=='cieszenie się na coś oczekiwanego':
                keys[n]='c.s.n.c.n'
            if i=='zaskoczenie czymś nieprzewidywanym':
                keys[n]='z.cz.n'
        plot=fig.add_subplot(2,2,order)
        plot.barh(keys,values, label=title, color=['r','r','r','r','r','g','g','g'])
        plt.title(title)
        order+=1
        positiveRatio=round((positive/total)*100,2)
        negativeRatio=round(100-positiveRatio,2)
        print(title + ': ' )
        print('Positive ratio: ' + str(positiveRatio) + '%')
        print('Negative ratio: ' + str(negativeRatio) + '%')
# plt.legend(loc='best')
plt.show()
#72x