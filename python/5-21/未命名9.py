# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:18:03 2023

@author: sunflower
"""

def getText(text):
    text = text.lower()                 # 将文本中字母全变为小写
    for ch in ",.;?-:\'":
        text = text.replace(ch, " ")   # 将文本中的标点符号替换为空格
    return text


def wordFreq(text,topn):  
# text为待统计文本，topn表示取频率最高的单词个数
    words  = text.split()    # 将文本分词
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
# 若该单词在字典中已经存在，则在原计数上加1，若该单词还未统计，则计数为1
    excludes = {'the','and','to','of','a','be'}
# 定义集合存放需要去除的无意义单词
    for word in excludes:
        del(counts[word])    # 在字典中删除无意义单词
    items = list(counts.items())  # 将字典转换为列表，以方便排序
    items.sort(key=lambda x:x[1], reverse=True)
# 按照单词频率计数的逆序排序
    return items[:topn]  # 返回出现频率前topn的单词和频率计数值


#编写主程序，调用函数
try:
    with open("hamlet.txt",'r') as file:
        text = file.read()
        text = getText(text)
        freqs = wordFreq(text,10)
except IOError:
    print("文件不存在,请确认!\n")
else:
    try:
        with open("hamlet_w.txt",'w')as fileFreq:
                items =[ word + '\t' + str(freq) + '\n' for word,freq in freqs]
                fileFreq.writelines(items)
    except IOError:
        print("写入文件出错")
        for word,freq in freqs:
            print("{:<10}{:>}".format(word, freq))
