import urllib.parse, json, urllib.request, time
#-*- coding: utf-8 -*-

data = dict()

# out_path= '../wyniki/'
l='any2txt|wcrft2({"morfeusz2":true})|wsd|sentiment'
u='IKedracka'
t="Powiedziała mamie, że ją kocha"
s=dict(lpmn=l, text=t, user=u)

data['text']=t
data['lpmn']=l
data['user']="IKedracka"
doc=json.dumps(data).encode('utf8')

link="http://ws.clarin-pl.eu/nlprest2/base/startTask/"
u=urllib.parse.urlparse(link)
url=u.geturl()
base='http://ws.clarin-pl.eu/nlprest2/base'
tid = urllib.request.urlopen(urllib.request.Request(url,data=doc, headers={'Content-Type': 'application/json'})).read().decode('utf8')
time.sleep(3)
print(tid)
resp = urllib.request.urlopen(urllib.request.Request(base + '/getStatus/' + tid)).read()
data=json.loads(resp)
results=data['value']
print(results)


for item in results:
    content = urllib.request.urlopen(urllib.request.Request(base + '/download' + item['fileID'])).read().decode('utf8')
    print(item['name'] + " content: " + content)
    # try:
    #     with open(out_path + item['name'] + '_filter_fls.ccl', "w") as outfile:
    #         outfile.write(content)
    # except OSError as e:
    #     print(item['name'] + ' - exception error')
