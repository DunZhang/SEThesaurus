# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 23:16:50 2019

@author: Administrator
"""
from os.path import join,dirname
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
from gensim.models.phrases import Phrases, Phraser
from gensim.models.word2vec import LineSentence,Word2Vec
PROJ_PATH = dirname(dirname(__file__))
import json
from DST.phrase_detection.PhraseDetection import PhraseDetection,TxtIter




if __name__ == "__main__":
    ######################################get phrase text##################################333
#    phrase_detection_wiki = PhraseDetection(savePhraserPaths = [join(PROJ_PATH,"data/phrase_model/wiki_2gram_10_15.0_def.phraser"),
#                                                                join(PROJ_PATH,"data/phrase_model/wiki_3gram_10_15.0_def.phraser")], 
#                                            file_overwrite=False,
#                                            min_count=10,
#                                            threshold=15.0,
#                                            max_vocab_size=120000000, 
#                                            delimiter=b'_', 
#                                            scoring='default', 
#                                            wordNumInPhrase=3)
#    phrase_detection_wiki.fit(sentencesPath="C:/SE/step1.1_wiki_for_phrase.txt")
#    
#    phrase_detection_wiki.transform(sentencesPath="C:/SE/step1.1_wiki_for_phrase.txt",
#                                    savePath=join(PROJ_PATH,"data/step1.3_wiki_phrase.txt"))
    
#    phrase_detection_wiki = PhraseDetection(savePhraserPaths = [join(PROJ_PATH,"data/phrase_model/so_2gram_10_15.0_def.phraser"),
#                                                                join(PROJ_PATH,"data/phrase_model/so_3gram_10_15.0_def.phraser")], 
#                                            file_overwrite=False,
#                                            min_count=10,
#                                            threshold=15.0,
#                                            max_vocab_size=120000000, 
#                                            delimiter=b'_', 
#                                            scoring='default', 
#                                            wordNumInPhrase=3)
#    phrase_detection_wiki.fit(sentencesPath="C:/SE/step1.2_so_for_phrase.txt")
#    
#    phrase_detection_wiki.transform(sentencesPath="C:/SE/step1.2_so_for_embed.txt",
#                                    savePath=join(PROJ_PATH,"data/step1.3_so_phrase.txt")) 
    #####################################get vocab#########################################
    so_vocab = {}
    with open(join(PROJ_PATH,"data/step1.3_so_phrase.txt"),"r",encoding = "utf-8") as fr:
        for line in fr:
            for word in line.split():
                if word in so_vocab:
                    so_vocab[word]+=1
                else:
                    so_vocab[word]=1
    with open(join(PROJ_PATH,"data/step1.3_so_vocab.json"),"w",encoding = "utf-8") as fw:
        json.dump(so_vocab,fw)
    
    wiki_vocab = {}
    with open(join(PROJ_PATH,"data/step1.3_wiki_phrase.txt"),"r",encoding = "utf-8") as fr:
        for line in fr:
            for word in line.split():
                if word in wiki_vocab:
                    wiki_vocab[word]+=1
                else:
                    wiki_vocab[word]=1
    with open(join(PROJ_PATH,"data/step1.3_wiki_vocab.json"),"w",encoding = "utf-8") as fw:
        json.dump(wiki_vocab,fw) 
    

#####################################read vocab#########################################  
#    with open(join(PROJ_PATH,"data/step1.3_so_vocab.json"),"r",encoding = "utf-8") as fr:
#        so_vocab = json.load(fr)
    soc = []
    for k,v in so_vocab.items():
        if v>10:
            soc.append(k)
    
#    with open(join(PROJ_PATH,"data/step1.3_so_vocab.json"),"r",encoding = "utf-8") as fr:
#        so_vocab = json.load(fr)
    wikic = []
    for k,v in wiki_vocab.items():
        if v>10:
            wikic.append(k)      
        
#    t1=0
#    for k,v in so_vocab.items():
#        t1+=v
#    t2=0
#    for k,v in di.items():
#        t2+=v   
#    
    
    
    
    
    
