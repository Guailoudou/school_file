def GetText(text):
    text = text.lower()
    for c in ",.;?-:\'":
        text = text.replace(c, " ")
    return text
def wordFrep(text,topn):
    text = GetText(text)
    words = text.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    excludes = {'the','and','to','of','a','be'}
    for word in excludes:
        if word in word_freq:
            del(word_freq[word])
    word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return word_freq[:topn]
def sy6_6():
    text = """I have a dream today!I have a dream that one day every valley shall be exalted, and every hill and mountain shall be made low, the rough places will be made plain, and the crooked places will be made straight; "and the glory of the Lord shall be revealed and all flesh shall see it together." This is our hope, and this is the faith that I go back to the South with.With this faith, we will be able to hew out of the mountain of despair a stone of hope. With this faith, we will be able to transform the jangling discords of our nation into a beautiful symphony of brotherhood. With this faith, we will be able to work together, to pray together, to struggle together, to go to jail together, to stand up for freedom together, knowing that we will be free one day."""
    for word,freq in wordFrep(text,10):
        print(word,freq)

dicStus={'李明':('男',19),'杨柳':('女',18),'张一凡':('男',18), '许可':('女',20),'王小小':('女', 19),'陈心':('女',19)}
def sy6_7():
    names = []
    cnt ={}
    for name,info in dicStus.items():
        #统计男女数量和大于18的人数
        cnt[info[0]] = cnt.get(info[0],0)+1
        if info[1]>18:
            names.append(name)
    print(cnt)
    print(names)
def sy6_8():
    dicBoys={'江苏':8,'浙江':5,'山东':5,'安徽':4,'福建':2} 
    dicGirls={'江苏':3,'浙江':2,'吉林':1}
    #合并
    dic={}
    dic.update(dicBoys)
    for k,v in dicGirls.items():
        dic[k]=dic.get(k,0)+v
    for k,v in dic.items():
        print(k,v)
def sy6_9():
    ls=[{'性别':'女','书本':10,'文具':30,'服饰':300,'零食':150,'日用品':600}, {'性别':'女','书本':200,'文具':10,'服饰':300,'零食':300,'日用品':100}, {'性别':'男','书本':200,'文具':100,'服饰':1000,'零食':100,'日用品':200}, {'性别':'男','书本':50,'文具':20,'服饰':300,'零食':150,'日用品':600}, {'性别':'男','书本':200,'文具':50,'服饰':400,'零食':100,'日用品':200}, {'性别':'女','书本':100,'文具':10,'服饰':500,'零食':150,'日用品':800}, {'性别':'女','书本':200,'文具':100,'服饰':500,'零食':300,'日用品':200}, {'性别':'男','书本':300,'文具':50,'服饰':0,'零食':10,'日用品':50}, {'性别':'男','书本':100,'文具':10,'服饰':500,'零食':40,'日用品':500}, {'性别':'男','书本':200,'文具':50,'服饰':200,'零食':100,'日用品':100}]
    #统计每一类项目的平均消费金额
    dic={}
    xb={}
    xbm={}
    isn = True
    for dicItem in ls:
        for k,v in dicItem.items():
            if k=='性别':
                xb[v]=xb.get(v,0)+1
                if v=='女':
                    isn = False
                else:
                    isn = True
            if k!='性别':
                dic[k]=dic.get(k,0)+v
                if isn:
                    xbm['男']=xbm.get('男',0)+v
                else:
                    xbm['女']=xbm.get('女',0)+v
    data1 = {}
    data2 = {}
    for k,v in dic.items():
        data1[k]=v/len(ls)
    for k,v in xbm.items():
        data2[k]=v/xb[k]
    print(data1)
    print(data2)


def sy6_10():
    tables = {

        '萧峰': {'筋骨': 20, '敏捷': 17, '气势': 20, '反应': 20, '技巧': 18, '内力': 19},

        '杨过': {'筋骨': 18, '敏捷': 19, '气势': 17, '反应': 20, '技巧': 18, '内力': 18},

        '令狐冲': {'筋骨': 12, '敏捷': 17, '气势': 14, '反应': 20, '技巧': 19, '内力': 13},

        '张无忌': {'筋骨': 20, '敏捷': 17, '气势': 15, '反应': 14, '技巧': 20, '内力': 20},

        '郭靖': {'筋骨': 19, '敏捷': 18, '气势': 19, '反应': 18, '技巧': 19, '内力': 20}

        }
    #每人总分 1
    allmun = {}
    for k,v in tables.items():
        allmun[k]=sum(v.values())
    #每人平均分 2
    allavg = {}
    allavg = {k:v/len(tables) for k,v in allmun.items()}
    #各项属性总分
    avgm = {}
    for k,v in tables.items():
        for k1,v1 in v.items():
            avgm[k1]=avgm.get(k1,0)+v1
    #各项属性平均分 3
    avg={}
    avg = {k:v/len(tables) for k,v in avgm.items()}
    #总分排序 4
    allmunsort = sorted(allmun.items(),key=lambda x:x[1],reverse=True)
    print(allmun)
    print(allavg)
    print(avg)
    print(allmunsort)
sy6_10()