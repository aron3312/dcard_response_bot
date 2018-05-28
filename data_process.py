# -*- coding=utf-8 -*-
import jieba.posseg as pseg
import codecs
import io
import sys
from gensim import corpora
import os
import re
import json
import pickle
class D_card_corpus(object):
    def __init__(self):
        self.corpus = []
        stop_words = 'D:/stopwords22.txt'
        stopwords = codecs.open(stop_words,'r',encoding='utf8').readlines()
        self.stopwords = [ w.strip() for w in stopwords ]
        self.stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
    def open_data(self,filename):
        with open('data/'+filename+'.json') as json_data:
            articles = json.load(json_data)
        return articles
    def tokenization(self,text):
        result = []
        words = pseg.cut(text)
        for word, flag in words:
            if flag not in self.stop_flag and word not in self.stopwords:
                result.append(word)
        return result
    def from_articles_get_corpus(self,board):
        """
        word seg and create corpus or load corpus
        """
        articles = self.open_data(board)
        articles_content = [c['content'] for c in articles]
        if os.path.exists(board+"_corpus.pkl"):
            with open(board+'_corpus.pkl', 'rb') as pickle_load:
                self.corpus = pickle.load(pickle_load)
            return self.corpus
        else:
            articles_content = articles_content[1:800]
            for f in articles_content:
                print(u"已經加入了"+str(len(self.corpus))+u"則貼文進入詞庫")
                self.corpus.append(self.tokenization(f))
            print("Finish append")
            with open(board+'_corpus.pkl', 'wb') as pickle_file:
                pickle.dump(self.corpus, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
            return self.corpus
