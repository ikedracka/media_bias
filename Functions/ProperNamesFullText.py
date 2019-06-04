#-*- coding: utf-8 -*-

# Program to retrieve and parse proper names from headlines

import urllib.parse, json, urllib.request, time, csv
import xml.etree.ElementTree as et

titles=['Fronda','Gazeta','Interia','NCzas','Newsweek','Onet','Polityka','RMFPolska','RMFSwiat','TVN24','TVPInfo','WP','WPolityce','Wprost']

def properNames(): #source as path to csv file

    # Initialize dictionary for CLARIN analysis:
    data = dict()
    l = 'any2txt|wcrft2|liner2({"model":"top9"})'
    u = 'IKedracka'

    # Limit categories to locations, names and organizations:
    t=['nam_loc','nam_liv','nam_org']
    proper_names = []

    # Get text to parse:
    for title in titles:
        words=list()
        path = "C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\DataFull\\" + title + ".txt"
        source=open(path,"r")

        # Split into bag of words:
        words = source.read().split(',')
        text = ' '.join(words)
        text = text.replace("'", "")
        data['text']=text
        data['lpmn']=l
        data['user']=u
        doc=json.dumps(data).encode('utf8')
        link="http://ws.clarin-pl.eu/nlprest2/base/startTask/"
        u=urllib.parse.urlparse(link)
        url=u.geturl()
        base='http://ws.clarin-pl.eu/nlprest2/base'
        tid = urllib.request.urlopen(urllib.request.Request(url,data=doc, headers={'Content-Type': 'application/json'})).read().decode('utf8')

        # Request delay to avoid incorrect response:
        time.sleep(15)
        resp = json.loads(urllib.request.urlopen(urllib.request.Request(base + '/getStatus/' + tid)).read())
        value=resp['value']

        # Request response:
        for item in value:
            content = urllib.request.urlopen(urllib.request.Request(base + '/download' + item['fileID'])).read().decode('utf8')
            # print(content)
            root=et.fromstring(content)
            # print(root)

            # Find all elements which contain
            for tok in root.findall('.//tok'):
                if (tok.findtext('ann') is not None):
                    tags=tok.findall('ann')
                    for tag in tags:
                        if (tag.attrib['chan'] in t and tag.text != '0'):
                            lex=tok.find('lex')
                            base=lex.findtext('base')
                            if base not in proper_names:
                                proper_names.append(base)
    return proper_names

names=properNames()

# Save results to the file:
with open("C:\\Users\\Ilona\\PycharmProjects\\TestDataGenerator\\resultProperNames.json","w") as result:
    json.dump(names, result, ensure_ascii=False)