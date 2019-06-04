#-*- coding: utf-8 -*-

# Program to count number of headlines retrieved:

import csv

# Declare media titles:
titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

for title in titles:
    path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataReal\\" + title + ".csv"
    file=open(path,"r")
    reader=csv.reader(file)
    numberOfHeadlines=0
    for line in reader:
        if len(line)>0:
            numberOfHeadlines+=1

    # Display number of headlines - first row contains header:
    print(title + ": " + str(numberOfHeadlines-1))