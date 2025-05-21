import os
def getText(text):
    text = text.lower()   
    for ch in ",.;?-:\'":
        text = text.replace(ch, " ") 
    return text


def wordFreq(text,topn):  
    words  = text.split()    # 将文本分词
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    excludes = {'the','and','to','of','a','be'}
    for word in excludes:
        del(counts[word]) 
    items = list(counts.items())  
    items.sort(key=lambda x:x[1], reverse=True)

    return items[:topn]  

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
                print("写入文件成功")
    except IOError:
        print("写入文件出错")
        for word,freq in freqs:
            print("{:<10}{:>}".format(word, freq))
