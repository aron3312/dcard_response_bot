# -*- coding: UTF-8 -*-
import os
import json
def main():
    m = Dataprocess(board="fitness")
    m.select_need_post_comment()
    m.combine_comments_titles()
class Dataprocess(object):
    def __init__(self,board):
        self.board = board
        with open('data/'+board+'.json') as json_data:
            self.posts = json.load(json_data)
        with open('data/'+board+"_comments"+'.json') as json_data2:
            self.comments = json.load(json_data2)
    def select_need_post_comment(self):
        new = [p for p in self.posts if p['commentCount']>0]
        new2 = [m for m in self.comments if m['hiddenByAuthor']==False and m['hidden']==False]
        with open("data/"+self.board+"2.json", 'w') as ope:
            ope.write(json.dumps(new, indent=4, ensure_ascii=False).encode('utf-8'))
        with open("data/"+self.board+"_comments2.json", 'w') as ope:
            ope.write(json.dumps(new2, indent=4, ensure_ascii=False).encode('utf-8'))
    def combine_comments_titles(self):
        with open('data/'+self.board+'2.json') as json_data:
            pro_posts = json.load(json_data)
        with open('data/'+self.board+"_comments2"+'.json') as json_data2:
            pro_comments = json.load(json_data2)
        title_comments = []
        for dat in pro_posts:
            dic = {}
            dic['id']=dat['id']
            dic['title']=dat['title']
            dic['all_comments'] = ' '.join([m['content'] for m in pro_comments])
            title_comments.append(dic)
            print('Already process '+str(len(title_comments))+" articles")
        with open("data/processed/"+self.board+"_processed.json", 'w') as ope:
            ope.write(json.dumps(title_comments, indent=4, ensure_ascii=False).encode('utf-8'))
#            [p['content'] for p in self.comments if p in ]
if __name__ == '__main__':
    main()
