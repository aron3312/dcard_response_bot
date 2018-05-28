# -*- coding: UTF-8 -*-
# -*- coding=utf-8 -*-
from data_process import D_card_corpus
import jieba.posseg as pseg
import codecs
import io
import sys
from gensim import corpora
from gensim.summarization import bm25
import os
import re
import json
import pickle
from get_query_data import get_queryset
from bm25 import bm25_model
import random
def main():

    chatter = DcardBot()
    #chatter.randomTalks(num=1000)
    chatter.chatTime()


class DcardBot(object):

    """
    Dcard回復機器人
    """

    def chatTime(self):
        print(u"Dcard Bot: 您好，請輸入想要回復的網址，我會幫您找出一個較好的回覆")
        while True:
            url = input("Dcard article url ")
            title = get_queryset().crawl_post_from_url(url)[0]
            print(u"Dcard Bot：您所想要回復的文章標題為："+title)
            print("Dcard Bot: " +random.choice(self.getResponse(board="dressup",url=url)).encode("BIG5","ignore"))
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
        all_response = D_card_corpus().open_data(board+"_comments")
        choosed_response = [p['content'] for p in all_response if p['postId']==post_id]
        return choosed_response
if __name__=="__main__":
    main()
