#-*- coding: utf-8 -*-

# Program to split words into syllables and calculate comprehensiveness' coefficient

# Declare titles:
titles=['NCzas','Newsweek','Onet','Polityka','WPolityce']
import pyphen, csv, re, math

# Declare handler to consume words and split into syllables:
dic=pyphen.Pyphen(lang='pl_PL')

for title in titles:
    path="C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\ArticleText\\" + title + "Text.txt"
    file=open(path)
    reader=csv.reader(file)

    # Declare pattern to remove all non-alphanumeric characters:
    pattern=re.compile('[\W_]+')
    sentLen=[]
    articleText=[]
    # Split into syllables:
    for line in reader:
        for item in line:
            sentences=item.split('.')
            for sentence in sentences:
                words=sentence.split(' ')
                words=list(filter(len, words))

                # Counter for counting words longer than 3 syllables:

                longerThan3=0
                for word in words:
                    word=pattern.sub('', word)
                    syllables=dic.inserted(word).split('-')
                    if len(syllables)>3:
                        longerThan3+=1
                if len(words)>0:
                    sen=[len(words), longerThan3]
                    sentLen.append(sen)

    numSentences=0
    wordsInSentence=0
    wordsLongerThan3=0

    # Iterate through sentences and number of long words they contain and save result in variables:
    for sentence in sentLen:
        # print(sentence)
        numSentences+=1
        wordsInSentence+=sentence[0]
        wordsLongerThan3+=sentence[1]

    # Calculate and display Pisarek coefficient:

    avgSentLength=wordsInSentence/numSentences
    percentageOfLongWords=wordsLongerThan3/wordsInSentence
    pisarek=math.sqrt(math.pow(avgSentLength,2) + math.pow(percentageOfLongWords,2))/2

    # Print result:
    print(title + ": " + str(round(pisarek,2)))






