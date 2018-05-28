# -*- coding=utf-8 -*-
from bm25 import bm25_model
import jieba.posseg as pseg
from data_process import D_card_corpus
from Crawler import Dcardcrawler
import json
import requests
import time
import urllib2, sys
import os
import codecs
class get_queryset(object):
    def __init__(self):
        self.url = "https://www.dcard.tw/_api/posts/"
        stop_words = 'D:/stopwords22.txt'
        stopwords = codecs.open(stop_words,'r',encoding='utf8').readlines()
        self.stopwords = [ w.strip() for w in stopwords ]
        self.stop_flag = ['x', 'c', 'u','d', 'p', 't', 'uj', 'm', 'f', 'r']
    def crawl_post_from_url(self,url):
        query_id = url.split("/p/")[1]
        m2=Dcardcrawler().get_req(self.url+query_id)
        content = D_card_corpus().tokenization(m2['content'])
        return [m2['title'],content,query_id]
