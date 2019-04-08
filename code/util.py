# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:30:49 2019

@author: Administrator
"""
import re
def word_token(sent):
    words = sent.split()
    res = []
    for word in words:
        if word[0] in ["'"]:
            word = word[1:]
        if len(word)<1:
            continue
        if word[-2:] == "s'":
            res.append(word[0:-1])
            res.append("'s")
        elif word[-2:] == "'s":
            res.append(word[0:-2])
            res.append("'s")  
        elif word[-1] in ["'"]:
            res.append(word[0:-1])
        else:
            res.append(word)
    return res