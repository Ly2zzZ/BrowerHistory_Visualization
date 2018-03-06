# -*- coding: utf-8 -*-
import os
import jieba
import codecs
import math
import json
import numpy
import sys
import time


def stopwordslist(filepath):
    stopwords = [line.strip() for line in codecs.open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

def save_file(path, str):
   # print path
    try:
        with codecs.open(path, "a", encoding='utf-8') as fout:
            fout.write(str)
    except:
        print "save error\n"

def separate(filepath, path2):
     try:
        f1 = codecs.open(filepath, "r", encoding='utf-8')
        text_content = f1.read()
        depart_words = jieba.cut(text_content)
        stopwords = stopwordslist('./stopwords.txt')
        outstr = ''
        for word in depart_words:
            if word not in stopwords:
                if word != '\t' and word != ' ' and word != '\n' and word != u'\u3000':
                    outstr += word
                    outstr += "/"
        #print outstr
        f1.close()
        save_file(path2, outstr)
     except:
         print "separate error\n"



def calc_tf(filepath, target):
    f1 = codecs.open(filepath, "r", encoding='utf-8')
    str1 = []
    for line in f1.readlines():
        linestr = line.strip('\r\n')
        linestr = linestr.replace(' ', '')
        linestrlist = linestr.split('/')
        str1 += linestrlist
    f1.close()


    Tf = 1.0
    tf = []
    Dictlist={}
    Numlist=[]

    for index in range(0, len(str1)):
        print index
        if str1[index] in Dictlist.keys():
            Dictlist[str1[index]]+=1
            Tf+=1
        else:
            Dictlist[str1[index]]=1
            Numlist.append(str1[index])
            Tf+=1


    keydict = sorted(Dictlist.iteritems(), key=lambda d: d[1], reverse=True)#关键词重要性排序


    out = codecs.open(target, "w", encoding='utf-8')

    keywords = ''
    for num in range(0, 100):   #提取TF值前50的关键词
        keywords += keydict[num][0]
        keywords += ','
        keywords += str(keydict[num][1]/Tf)
        keywords += '\r\n'

    out.write(keywords)

    out.close()

    pass




if __name__ == '__main__':
    filepath = "./blogCblog.txt"
    target_path = "./separate.txt"
    nn_path = './tf.txt'

    separate(filepath, target_path)

    calc_tf(target_path, nn_path)
