# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:41:52 2019

@author: Administrator
"""
import os
from os.path import join,isfile,isdir,dirname
from util import word_token
import regex,re
import codecs
import re
import logging

logger = logging.getLogger(__name__)
from lxml import etree
from bs4 import BeautifulSoup

PROJ_PATH = dirname(dirname(__file__))

    
class CleanDataSO(object):
    """
    class to clean StackOver flow data
    """

    def __init__(self, so_xml_path, clean_data_path, usage_scenario):
        """
        :param so_xml_path: the path of StackOver flow data, the data is big and
                can be downloaded from https://archive.org/download/stackexchange
        :param clean_data_path: save clean data to text file ( one line one sentence).
        """
        if usage_scenario == "phrase":   
            self.__reSub0 = re.compile("(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]")  # URL
            self.__reSub1 = re.compile("[\[\]<>`~$\^&*\"=|%@(){},:/\\\\]")  # replace with " "
            self.__resplit = re.compile("\.[^a-z0-9]|[?!;\n\r]")
            self.__rePlus = re.compile("[^+]\+[^+]")
            self.__minNum = 2
        elif usage_scenario == "embedding":
            self.__reSub0 = re.compile("(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]")  # URL
            self.__reSub1 = re.compile("[\[\]<>`~$\^&*\"=|%@(){}/\\\\]")  # replace with " "
            self.__resplit = re.compile("\.[^a-z0-9]|[,:?!;\n\r]")
            self.__rePlus = re.compile("[^+]\+[^+]")   
            self.__minNum = 5
            
        self.so_xml_path = so_xml_path
        self.clean_data_path = clean_data_path

    def __clean_data(self, strText):
        sentences = []
        strText = strText.lower()
        strText = re.sub(self.__reSub0, " ", strText)
        strText = re.sub(self.__reSub1, " ", strText)
        for sub in set(re.findall(self.__rePlus, strText)):
            strText = strText.replace(sub, sub[0] + " " + sub[2])
        for sentence in re.split(self.__resplit,strText):
            word_sen = word_token(sentence)
            if (len(word_sen) > self.__minNum):
                sentences.append(u" ".join(word_sen) + "\n")
        return sentences

    def transform(self):
        """
        clean data
        """
        logger.info("clean stack overflow data")
        context = etree.iterparse(self.so_xml_path, encoding="utf-8")
        fw = codecs.open(self.clean_data_path, mode="w", encoding="utf-8")

        clean_data = []  # 存储title 和 answers
        c = 0
        for _, elem in context:  # 迭代每一个
            c += 1
            if (c % 100000 == 0):
                logger.info("already clean record:" + str(c / 10000) + "W")
            title, body, typeId = elem.get("Title"), elem.get("Body"), elem.get("PostTypeId")
            elem.clear()
            if typeId is None or (int(typeId) != 1 and int(typeId) != 2):
                continue
            if body is not None:
                soup = BeautifulSoup(body, "lxml")
                for pre in soup.find_all("pre"):
                    if (len(pre.find_all("code")) > 0):
                        pre.decompose()
                clean_data.extend(self.__clean_data(soup.get_text()))
            if title is not None:
                clean_data.extend(self.__clean_data(BeautifulSoup(title, "lxml").get_text()))
            if len(clean_data) > 100000:  # write to local
                fw.writelines(clean_data)
                clean_data = []
        if len(clean_data) > 0:
            fw.writelines(clean_data)
        fw.close() 
if __name__ == "__main__":
    clean_so = CleanDataSO(so_xml_path=join(PROJ_PATH,"data/Posts.xml"),
                           clean_data_path=join(PROJ_PATH,"data/step1.2.txt"),
                           usage_scenario = "phrase")
    clean_so.transform()
#p = join(PROJ_PATH,"data/step1.2.1_so.txt")

#c = 0
#res = []
#with open(p,"r",encoding="utf-8") as fr:
#    for line in fr:
#        c+=1
#        if c>65656:
#            res.append(line)
#        if len(res)>6530:
#            break
#with open("E:/ll.txt","w",encoding="utf-8") as fw:
#    fw.writelines(res)
