# -*- coding: UTF-8 -*-
a = [0,3,5,7,9]
del a[0]
print(a)
import json
with open('data/fitness_comments.json') as json_data:
    d = json.load(json_data)
at = []
for k in d:
    if str(k['postId'])=="228121608":
        at.append(k)
print(len(at))


board = 'fitness'
with open('data/'+board+'.json') as json_data:
    posts = json.load(json_data)
with open('data/'+board+"_comments"+'.json') as json_data2:
    comments = json.load(json_data2)
print(len(posts))
new = [p for p in posts if p['commentCount']>0]
print(len(new))

new2 = [m for m in comments if m['hiddenByAuthor']==False and m['hidden']==False]

title_comments = []
for dat in new:
    dic = {}
    dic['id']=dat['id']
    dic['title']=dat['title']
    print(dat['id'])
    print([p['content'] for p in new2 if str(p['postId']) in str(dic['id']) ])
