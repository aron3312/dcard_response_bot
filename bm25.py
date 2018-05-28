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

class bm25_model(object):
    def __init__(self,board):
        self.corpus = D_card_corpus().from_articles_get_corpus(board)
    def get_most_similarity_article(self):
        """
        透過文章corpus取得average_idf，以便後續計算相關
        """
        dictionary = corpora.Dictionary(self.corpus)
        bm25Model = bm25.BM25(self.corpus)
        average_idf = sum(map(lambda k: float(bm25Model.idf[k]), bm25Model.idf.keys())) / len(bm25Model.idf.keys())
        return [bm25Model,average_idf]
