# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 20:30:49 2019

@author: Administrator
"""
import re
import random
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

def random_read(path):
    res = []
    c=0
    t = random.randint(1,426464)
    with open(path,"r",encoding="utf-8") as fr:
        for line in fr:
            c+=1
            if c>t:
                res.append(line)
            if len(res)>80:
                break
    return res