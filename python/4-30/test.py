# dicGDP={'2022年': 1210207.2, '2021年': 1149237.0, '2020年': 1013567.0}
# ls = sorted(dicGDP)
# for i in ls:
#     print(i,dicGDP[i])
# t = list(dicGDP.items())
# t.sort(key=lambda x:x[1],reverse=True)
# print(t)


# dicAreas= {'俄罗斯': 1707.5, '加拿大': 997.1, '中国': 960.1, '美国': 936.4, '巴西': 854.7}
# dicCapitals={'俄罗斯': '莫斯科', '加拿大': '渥太华', '中国': '北京', '美国': '华盛顿', '巴西': '巴西利亚'}
# dim = {}
# for i in dicAreas.keys():
#     dim[i] = [dicAreas[i],dicCapitals[i]]
# print(dim)
# for i in dim.items():
#     print(i)


# dicGDP={'2022年':1210207.2, '2021年':1149237.0, '2020年':1013567.0, '2019年':986515.2, '2018年': 919281.1}
# dicPopulation={'2022年':141217.5, '2021年':141236, '2020年':141110, '2019年':140774.5,'2018年':140276}
# dicNew={}
# for k,v  in dicGDP.items():
#     dicNew[k] = [v,dicPopulation[k]]
# print(dicNew)

# set1 = {(1,2),(3,4)}
# print(set1)
# list=[1,2,3,4]
# set2 = set(list)
# print(set2)

import random
ls = []
for i in range(20):
    ls.append(random.randint(0,20))
print(ls)
set3 = set(ls)
print(set3)

ls2 = [random.randint(0,20) for i in range(20)]
ste4 = set(ls2)
print(ls2)
print(ste4)

setI = {'Python','C++','C','Java','C#'}
setT = {'C++','C','Java','C#','JavaScript'}
print(setI & setT)
print(setI | setT)
print(setI - setT)
print(setI ^ setT)

listt = {}
name = input('请输入姓名：')

listt[name] = [input('：'),input('：'),input('：')]

for k,v in listt.items():
    print(k,v[0],v[1],v[2])
