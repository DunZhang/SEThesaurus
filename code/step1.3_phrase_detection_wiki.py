# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 23:16:50 2019

@author: Administrator
"""
from os.path import join,dirname
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
from gensim.models.phrases import Phrases, Phraser
from gensim.models.word2vec import LineSentence
PROJ_PATH = dirname(dirname(__file__))

from DST.phrase_detection.PhraseDetection import PhraseDetection




if __name__ == "__main__":
    phrase_detection_wiki = PhraseDetection(savePhraserPaths = [join(PROJ_PATH,"data/phrase_model/wiki_pd_2n_10_15.0_def.model"),
                                                                join(PROJ_PATH,"data/phrase_model/wiki_pd_3n_10_15.0_def.model")], 
                                            file_overwrite=False,
                                            min_count=10,
                                            threshold=15.0,
                                            max_vocab_size=120000000, 
                                            delimiter=b'_', 
                                            scoring='default', 
                                            wordNumInPhrase=3)
    phrase_detection_wiki.fit(sentencesPath=join(PROJ_PATH,"data/step1.1_wiki_for_phrase.txt"))
    phrase_detection_wiki.transform(sentencesPath=join(PROJ_PATH,"data/step1.1_wiki_for_phrase.txt"),
                                    savePath=join(PROJ_PATH,"data/step1.3_wiki_phrase.txt"))