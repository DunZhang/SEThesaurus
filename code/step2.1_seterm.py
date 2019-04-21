# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:46:07 2019

@author: Administrator
"""

from os.path import join,dirname
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
import json
import re
logger = logging.getLogger(__name__)
from DST.domain_term.DomainTerm import DomainTerm
PROJ_PATH = dirname(dirname(__file__))


def filterTerm(term):
    try:
        term.encode(encoding="ascii")
    except:
        return False

    if len(term) == 1 and term != "r" and term != "c":
        return False
    if term[-1] == "." or term[-1] == "_":
        return False
    # the term cannot include these punctuations
    special_list = ["@", "*", "[", "]", "=", ">", "<", "\\", "/", "|", "&", "$", "~", "^", "%", "..", "--", "__", "`",
                    "´", "’", "‘", "“", "”", " ", "£", "¿", "www.", ".com", "test.", "slow", "'s", ".org", ".axd",
                    ".app",
                    ".mail", ".test", ".mf", ".location",
                    ".system", ".imageio", ".io", ".beginform", ".futures", ".mappath", ".drawing", ".observablearray",
                    ".conf", ".table",
                    ".path", ".actionlink", ".settings", ".log", ".util", ".concurrent"]
    for i in special_list:
        if i in term:
            return False
    # remove terms whose begining is
    firstLetter_set = set(["#", "_", "+", "-"])
    if term[0] in firstLetter_set:
        return False
    # remove terms whose first character is a digit except some special cases
    if len(re.findall(r"\d\.\d", term)) > 0:  # no version number such as "3.2.1"
        return False

    signal = False  # fail if there are no letters in the term
    for character in term:
        if character.isalpha():
            signal = True
            break
    return signal





if __name__ == "__main__":
    with open(join(PROJ_PATH,"data/step1.3_so_vocab.json"),"r",encoding = "utf-8") as fr:
        so_vocab = json.load(fr)
    with open(join(PROJ_PATH,"data/step1.3_wiki_vocab.json"),"r",encoding = "utf-8") as fr:
        wiki_vocab = json.load(fr)
    domain_term = DomainTerm(maxTermsCount=500000, thresholdScore=80.0, 
                             freqRangeDomainVocab=(15, float("inf")), 
                             freqRangeGeneralVocab=(15, float("inf")),
                             filterTermFunc=filterTerm)
    seterms = domain_term.extract_term(so_vocab,wiki_vocab)
#    so_count = 12891239
#    wiki_count = 8705110
##    for _,v in so_vocab.items():
##        so_count+=1
##    for _,v in wiki_vocab.items():
##        wiki_count+=1
#    
#    seterm = []
#    
#    for k,v in so_vocab.items():
#        if v<10:
#            continue
#        if k not in wiki_vocab:
#            seterm.append(k)
#        elif (v/so_count)/(wiki_vocab[k]/wiki_count)>20.0:
#            seterm.append(k)
#        
        
        
        
        
        
        
        
    
        