# Categorize proper names into political parties
# Load proper names to array
# Select sentences with proper names among all sentences
# Calculate summary for emotional words for each party

import csv

properNames=[]
source=open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\resultProperNames.json")
words=set(source.read().split())
for word in words:
    properNames.append(word.replace('"','').replace(',',''))

print(properNames)
