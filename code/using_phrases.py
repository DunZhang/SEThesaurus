# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:28:42 2019

@author: Administrator
"""
from gensim.models.phrases import Phraser,Phrases




sen = [["A","B","C","D"],["A","B","F","G"],["A","B","V","V"]]
sen1 = [["B","C","D"],["B","C","G"]]
p = Phrases(min_count = 1,threshold=1)
p.add_vocab(sen)


p.threshold = 1

p.add_vocab(sen1)

t = p.export_phrases(["B","C","C"])
for i in t:
    print(i)
