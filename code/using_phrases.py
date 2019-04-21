# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:28:42 2019

@author: Administrator
"""
from gensim.models.phrases import Phraser,Phrases




sen = [["A","B","C","D"],["A","B","F","G"],["A","B","V","V"]]
#sen1 = [["B","C","D"],["B","C","G"]]
p = Phrases(sen,min_count = 1,threshold=1)
p1 = Phraser(p)


p1.threshold = 3
p1.save()
Phrase
print( p1[["A","B","C"]] )

