# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:46:07 2019

@author: Administrator
"""

from os.path import join,dirname
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)
from gensim.models import Word2Vec, FastText
from gensim.models.word2vec import LineSentence
PROJ_PATH = dirname(dirname(__file__))








if __name__ == "__main__":
    ls = LineSentence(join(PROJ_PATH,"data/step1.2_so_for_embed.txt"))
    skip_gram = Word2Vec(sentences=ls,min_count=5, size=200, sg=1, window=5, workers = 7)
    skip_gram.delete_temporary_training_data(True)
    skip_gram.save(join(PROJ_PATH,"data/skipgram/skipgram.model"))

    ls = LineSentence(join(PROJ_PATH,"data/step1.2_so_for_embed.txt"))
    ff = FastText(sentences=ls,min_count=5, size=200, sg=1, window=5,workers = 7)
    ff.save(join(PROJ_PATH,"data/fasttext/fasttext.model"))