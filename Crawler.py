# -*- coding: UTF-8 -*-
import json
import requests
import time
import urllib2, sys
import os

def main():
    crawler = Dcardcrawler()

    crawler.crawl_posts(board=sys.argv[1])
    # articles = crawler.open_data("talk")
    # a = map(crawler.get_post_response,[p['id'] for p in articles][0:5])
    # print(len(a))
class Dcardcrawler(object):
    root_url = "https://www.dcard.tw/_api/"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    def __init__(self):
        self.art_url = self.root_url+"posts/"
    def get_req(self,url):
        """
        對url發出request以及解讀json response
        """
        try:
            req = urllib2.Request(url,headers=self.hdr)
        except:
            req = urllib2.Request(url,headers=self.hdr)
        try:
            response = urllib2.urlopen(req)
        except:
            response = urllib2.urlopen(req)
        data2 = json.loads(response.read().decode('utf-8'))
        return data2

    def get_id(self,data2):
        """
        獲取文章id以便查詢內文
        """
        for d in data2:
            yield(self.art_url+str(d['id']))

    def open_data(self,filename):
        with open('data/'+filename+'.json') as json_data:
            articles = json.load(json_data)
        return articles

    def output(self, filename, data):
        """
        輸出
        """
        with open("data/"+filename+".json", 'w') as ope:
            ope.write(json.dumps(data, indent=4, ensure_ascii=False).encode('utf-8'))

    def crawl_posts(self,board):
        self.board = board
        self.form_url = self.root_url+"forums/"+board+"/posts?"
        if os.path.exists("data/"+self.board+".json"):
            final=self.open_data(board)
            pp_id = final[len(final)-1]['id']
            m = self.get_req(self.form_url+"&before="+str(pp_id))
            allid = [self.art_url+str(a['id']) for a in m ]
            [final.append(self.get_req(p)) for p in allid]
            while len(allid)==30:
                pp_id = final[len(final)-1]['id']
                m = self.get_req(self.form_url+"&before="+str(pp_id))
                allid = [self.art_url+str(a['id']) for a in m ]
                [final.append(self.get_req(p)) for p in allid]
                self.output(self.board,final)
                print("Already crawl "+str(len(final))+" articles")
        else:
            final = []
            m = self.get_req(self.form_url)
            allid = [self.art_url+str(a['id']) for a in m ]
            [final.append(self.get_req(p)) for p in allid]
            while len(allid)==30:
                pp_id = final[len(final)-1]['id']
                m = self.get_req(self.form_url+"&before="+str(pp_id))
                allid = [self.art_url+str(a['id']) for a in m ]
                [final.append(self.get_req(p)) for p in allid]
                self.output(self.board,final)
                print("Already crawl "+str(len(final))+" articles")
    def get_post_response(self,id):
        url = "https://www.dcard.tw/_api/posts/"+str(id)+"/comments"
        m3  = self.get_req(url)
        if len(m3)==30:
            c_num = 0
            result = []
            while len(m3)==30:
                [result.append(a) for a in m3]
                m3 = self.get_req(p_id+"/comments?after="+str(c_num))
                print("Already crawl "+str(len(result))+" comments")
            return(result)
        else:
            print("Already crawl "+str(len(m3))+" comments")
            return(m3)

        #for t in result:
        #    final.append(t)
        #for i in range(self.page):
        #    pp_id = result[len(result)-1]['id']
        #    result = []
        #    m = self.get_req(self.form_url+"&before="+str(pp_id))
        #    for p_id in self.get_id(m):
        #        m2 = self.get_req(p_id)
        #        m3 = self.get_req(p_id+"/comments")
        #        result.append(m2)
        #        for abc in m3:
        #            comment.append(abc)
        #        if len(m3)>29:
        #            c_num=0
        #            while (len(m3)==30):
        #                c_num = c_num+30
        #                m3 = self.get_req(p_id+"/comments?after="+str(c_num))
        #                for abc in m3:
        #                    comment.append(abc)
        #    for t in result:
        #        final.append(t)
        #    for tt in comment:
        #        allcomment.append(tt)
        #    self.output(self.board,final)
        #    self.output(self.board+"_comments",allcomment)
        #    print("Already crawl "+str(i+1)+" pages")
        #    print("Already crawl "+str(len(final))+" articles")
        #    print("Already crawl "+str(len(allcomment))+" comments")

if __name__ == '__main__':
    main()
