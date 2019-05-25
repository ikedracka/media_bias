import json, csv
import pandas as pd

from Functions.RandomStringDigits import randomStringDigits


file=open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\Fronda.csv", "r")
data=csv.DictReader(file)
# for line in data:
    # for key, value in line.items():
        # print(key, value)
# create PD dataframe with unique key

df=pd.DataFrame(columns=['key', 'source','headline','timestamp'])
for record in data:
    id=randomStringDigits(8)
    title=record['Title']
    headline=record['Headline']
    timestamp=record['Timestamp']
    line=pd.DataFrame({'key':[id], 'source':[title],'headline':[headline], 'timestamp':[timestamp]})
    df=df.append(line)

print(df.to_string())
#lematyzacja i prosta identyfikacja poszczególnych s³ów
# najczêstsze s³owa w poszczególnych Ÿród³ach