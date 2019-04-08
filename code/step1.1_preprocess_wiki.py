# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 00:33:37 2019

@author: Administrator
"""
import os
from os.path import join,isfile,isdir,dirname
from util import word_token
import regex,re
PROJ_PATH = dirname(dirname(__file__))
class CleanDataWiki(object):
    """
    class to clean StackOver flow data
    """

    def __init__(self, wiki_paths, clean_data_path):
        self.__reSub0 = re.compile("(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]")  # URL
        self.__reSub1 = re.compile("[\[\]<>`~$\^&*\"=|%@(){}/\\\\]")  # replace with " "
        self.__bracket = r"\((?:[^()]++|(?R))*+\)"
        self.wiki_paths = wiki_paths
        self.clean_data_path = clean_data_path

    def __clean_data(self, strText):
        sentences = []
        strText = strText.lower()
        strText = regex.subf(self.__bracket,"",strText)
        strText = re.sub(self.__reSub0, " ", strText)
        strText = re.sub(self.__reSub1, " ", strText)
        
        
        for sentence in re.split("\.[^a-z0-9]|[,:?!;\n\r]",strText):
            word_sen = word_token(sentence)
            if (len(word_sen) > 3):
                sentences.append(u" ".join(word_sen) + "\n")
        return sentences

    def transform(self,batch_size=100000):
        data = []
        fw = open(self.clean_data_path,"w",encoding="utf-8")
        for path in self.wiki_paths:
            print(path)
            with open(path,"r",encoding="utf-8") as fr:
                for line in fr:
                    if line.startswith("<doc") or line.startswith("</doc>") or " " not in line:
                        continue
                    data.extend(self.__clean_data(line))
                    if len(data)>batch_size:
                        fw.writelines(data)
                        data = []
        fw.writelines(data)
        fw.close()

def getAllFilePaths(dirPath):
    return [os.path.join(dirPath,filePath) for filePath in os.listdir(dirPath) if isfile(join(dirPath,filePath))]
                    

if __name__ == "__main__":
    
    clean_wiki = CleanDataWiki(wiki_paths = getAllFilePaths(join(PROJ_PATH,"data/text/AA")),
                               clean_data_path = join(PROJ_PATH,"data/step1.1_wiki.txt"))
    clean_wiki.transform(100000)
    