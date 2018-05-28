# -*- coding: UTF-8 -*-
# -*- coding=utf-8 -*-
from data_process import D_card_corpus
import jieba.posseg as pseg
import codecs
import io
import sys
from gensim import corpora
from Crawler import Dcardcrawler
from gensim.summarization import bm25
import os
import re
import json
import pickle
from get_query_data import get_queryset
from bm25 import bm25_model
from itertools import chain
import random

def main():
    chatter = DcardBot()
    #chatter.randomTalks(num=1000)
    chatter.chatTime(board=sys.argv[1])


class DcardBot(object):

    """
    Dcard回復機器人
    """

    def chatTime(self,board):
        print(u"Dcard Bot: 您好，稍等一下確認語詞庫")
        D_card_corpus().from_articles_get_corpus(board)
        print(u"Dcard Bot: 您好，請輸入想要回復的網址，我會幫您找出一個較好的回覆")
        while True:
            url =  raw_input("Dcard article url ")
            if url == "exit":
                break
            while "www" not in url:
                print(u"Dcard Bot：你貼的不是網址喔")
                url = raw_input("Dcard article url ")
                if url == "exit":
                    break
            if url == "exit":
                break
            try:
                title = get_queryset().crawl_post_from_url(url)[0]
                print(u"Dcard Bot：您所想要回復的文章標題為："+title)
                print("Dcard Bot: " +random.choice(self.getResponse(board=board,url=url)).encode("BIG5","ignore"))
            except:
                print(u"Dcard Bot：這個網址找不到結果")

    def getResponse(self,board,url):
        query = get_queryset().crawl_post_from_url(url)[1]
        average_idf = bm25_model(board).get_most_similarity_article()[1]
        bm25Model = bm25_model(board).get_most_similarity_article()[0]
        scores = bm25Model.get_scores(query,average_idf)
        articles = D_card_corpus().open_data(board)
        # scores.sort(reverse=True)
        scores_ordered = sorted(scores,reverse=True)
        while articles[scores.index(scores_ordered[0])]['commentCount']==0 or  get_queryset().crawl_post_from_url(url)[2]==articles[scores.index(scores_ordered[0])]['id']:
            del scores_ordered[0]
        idx =  scores.index(scores_ordered[0])
        post_id =  articles[idx]['id']
        print(u"幫你找到最相似的文章標題為：".encode("BIG5","ignore")+articles[idx]['title'].encode("BIG5","ignore"))
        # all_response = D_card_corpus().open_data(board+"_comments")
        # choosed_response = [p['content'] for p in all_response if p['postId']==post_id]
        choosed_response = Dcardcrawler().get_post_response(post_id)
        keys = set(chain.from_iterable(choosed_response))
        for item in choosed_response:
            item.update({key: None for key in keys if key not in item})
        a = [p['content'] for p in choosed_response]
        return a
if __name__=="__main__":
    main()
