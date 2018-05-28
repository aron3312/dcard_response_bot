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


query = get_queryset().crawl_post_from_url("https://www.dcard.tw/f/fitness/p/228435078")
average_idf = bm25_model("fitness").get_most_similarity_article()[1]
bm25Model = bm25_model("fitness").get_most_similarity_article()[0]
scores = bm25Model.get_scores(query,average_idf)
articles = D_card_corpus().open_data("fitness")
# scores.sort(reverse=True)
scores_ordered = sorted(scores,reverse=True)
while articles[scores.index(scores_ordered[0])]['commentCount']==0 :
    del scores_ordered[0]
idx =  scores.index(scores_ordered[0])
post_id =  articles[idx]['id']
print(articles[idx]['content'].encode("big5","ignore"))
print(post_id)
all_response = D_card_corpus().open_data("fitness_comments")

choosed_response = [p['content'] for p in all_response if p['postId']==post_id]
print(random.choice(choosed_response).encode("BIG5","ignore"))
