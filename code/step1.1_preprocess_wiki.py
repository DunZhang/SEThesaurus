# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 00:33:37 2019

@author: Administrator
"""
import os
from os.path import join,isfile,isdir,dirname
import nltk
from nltk import sent_tokenize,word_tokenize,wordpunct_tokenize
import regex,re
import string
PROJ_PATH = dirname(dirname(__file__))

def word_token(sent,punt):
    words = word_tokenize(sent.replace("#","A"))
    words = [word.replace("A","#") for word in words if word not in punt]
    return words
def sent_token(text,punt):
    text = text.lower()
    text = regex.subf(r"\((?:[^()]++|(?R))*+\)","",text)
    return [ u" ".join(word_token(sent,punt))+"\n" for sent in sent_tokenize(text)]
def main(paths,savePath,batch_size):
    data = []
    punt = set(string.punctuation)
    punt.add("`")
    punt.add("''")
    punt.add("'")
    punt.add("``")
    fw = open(savePath,"w",encoding="utf-8")
    for path in paths:
        print(path)
        with open(path,"r",encoding="utf-8") as fr:
            for line in fr:
                if line.startswith("<doc") or line.startswith("</doc>") or " " not in line:
                    continue
                data.extend(sent_token(line,punt))
        if len(data)>batch_size:
            fw.writelines(data)
            data = []
    fw.writelines(data)
    fw.close()
def getAllFilePaths(dirPath):
    return [os.path.join(dirPath,filePath) for filePath in os.listdir(dirPath) if isfile(join(dirPath,filePath))]
                    

if __name__ == "__main__":
    
    main(paths=getAllFilePaths(join(PROJ_PATH,"data/test/AA")),
          savePath = join(PROJ_PATH,"data/step1.1_wiki.txt"),
          batch_size=100)
    
#    nltk.sent_tokenize("It took until 1980 for the .DSM-III to differentiate autism from childhood schizophrenia. In 1987, the DSM-III-R provided a checklist for diagnosing autism. In May 2013, the DSM-5 was released, updating the classification for pervasive developmental disorders. The grouping of disorders, including PDD-NOS, Autism, Asperger Syndrome, Rett Syndrome, and CDD, has been removed and replaced with the general term of Autism Spectrum Disorders. The two categories that exist are impaired social communication and/or interaction, and restricted and/or repetitive behaviors. The Internet has helped autistic individuals bypass nonverbal cues and emotional sharing that they find so hard to deal with, and has given them a way to form online communities and work remotely. Societal and cultural aspects of autism have developed: some in the community seek a cure, while others believe that autism is simply another way of being.")
#    nltk.sent_tokenize("as asd asda. sd asd asd 123. asd ada.")
#    nltk.word_tokenize("how' to 123. c++  ss \"dd\".")
#    nltk.wordpunct_tokenize("how to# tak-a dog's ss 'dd'.")
#    res = getAllFilePaths("D:/学习")
#    s = os.listdir("D:/学习")
