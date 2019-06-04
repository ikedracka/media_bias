#-*- coding: utf-8 -*-
# Program to parse headlines into bag of words in order to simplify further analysis:

import json, csv, re, string
import pandas as pd

from Functions.RandomStringDigits import randomStringDigits

# Declare media titles:
titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

for title in titles:
    words = list()
    path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\" + title + ".csv"
    source = open(path, "r")
    lines = csv.DictReader(source)

    # Transform into bag of words:
    for line in lines:
        text = line['Headline'].split(' ')
        for word in text:
            words.append(re.sub(r'\W+', '', word))

    # Declare path to save the file:
    fullPath="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataFull\\" + title + ".txt"

    # Save the file:
    with open(fullPath, 'w') as file:
        file.write(str(words))
    file.close()
