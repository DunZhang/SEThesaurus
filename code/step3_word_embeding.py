# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 01:24:21 2019

@author: Administrator
"""
from os.path import join,dirname
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
PROJ_PATH = dirname(dirname(__file__))

from gensim.models.word2vec import Word2Vec,LineSentence
from gensim.models import FastText
if __name__ == "__main__":
    ### training fasttext
#    Ls = LineSentence("C:/SE/step1.3_so_phrase.txt")
#    fasttext = FastText(sentences=Ls,sg = 1, size = 200, window=5, min_count=5)
#    fasttext.save(join(PROJ_PATH,"data/fasttext/fasttext.model"))
    
    ### training word2vec
    Ls = LineSentence("C:/SE/step1.3_so_phrase.txt")
    skipgram = Word2Vec(sentences=Ls,sg = 1, size = 200, window=5, min_count=5, workers=3)
    skipgram.save(join(PROJ_PATH,"data/skipgram/skipgram.model"))
    