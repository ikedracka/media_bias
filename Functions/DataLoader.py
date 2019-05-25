#-*- coding: utf-8 -*-
import json, csv, re, string
import pandas as pd

from Functions.RandomStringDigits import randomStringDigits
#['Dziennik','Fronda']
titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

for title in titles:
    words = list()
    path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\" + title + ".csv"
    source = open(path, "r")
    lines = csv.DictReader(source)
    for line in lines:
        text = line['Headline'].split(' ')
        for word in text:
            words.append(re.sub(r'\W+', '', word))
    print(type(words))
    fullPath="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataFull\\" + title + ".txt"

    with open(fullPath, 'w') as file:
        file.write(str(words))
    file.close()

# df=pd.DataFrame(columns=['key', 'source','headline','timestamp'])
# for record in data:
#     id=randomStringDigits(8)
#     title=record['Title']
#     headline=record['Headline']
#     timestamp=record['Timestamp']
#     line=pd.DataFrame({'key':[id], 'source':[title],'headline':[headline], 'timestamp':[timestamp]})
#     df=df.append(line)
#
# print(df.to_string())