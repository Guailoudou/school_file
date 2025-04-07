import random
def sy1():
    lst_who=['小马','小羊','小鹿']

    lst_where=['草地','电影院','听故事']
    lst_what=["看电影","听故事","吃晚饭"]
    a, b, c=random.randint(0, 2),random.randint (0, 2),random.randint (0, 2)
    sentence=lst_who[a]+"在"+lst_where[b]+lst_what[c]
    print(sentence)

def sy2():
    lst_monthdays=[31,28,31,30,31,30, 31,31,30,31,30,31]
    month=eval(input("请输入月份："))
    while month!=0:
        print("您好,{月份有{天！".format(month,lst_monthdays[month-1]))
        month=eval(input("请输入月份:"))
    print("程序结束！")

def sy3(n):
    list = []
    for i in range(n):
        if i == 0 or i == 1:
            list.append(1)
        else:
            list.append(list[i - 1] + list[i - 2])
    return list
    
def sy4():
    lst_busstop=["龙江新城市","阳光广场","汉江路","嫩江路","清凉山公园","拉萨路","五台山","莫愁路"]
    startStop=input("请输入起点站：")
    endStop=input("请输入终点站：")
    startIndex=lst_busstop.index(startStop)
    endIndex=lst_busstop.index(endStop)
    if startIndex>endIndex:
        print("您需要乘坐反方向线路。")
    else:
        print("从{}站前往{}站需要{}站。".format(startStop, endStop, endIndex-startIndex))

def sy6():
    lst_student=[["001","李梅",19],["002","刘祥",20],["003","张武",18]]
    lst_new=[["004","刘宁",20],["006","梁峰",19]]
    lst_student.extend(lst_new)
    lst_student.insert(4,["005","林歌",20])
    print("学号为003的学生信息：",lst_student[2])
    print("所有学生的姓名：",[x[1]for x in lst_student])
    print("年龄小于19的所有学生的信息：",[x for x in lst_student if x[2]>19])
def sy11():
    lst_info=[["李玉","男",25],["金忠","男",23],["刘妍","女",21],["莫心","女",24],["沈冲","男",28]]
    name=input("请输入您要删除信息的员工姓名：")
    while name!="0":
        for info in lst_info:
            if info[0]==name:
                lst_info.remove(info)
                print("删除后的列表：{}".format(lst_info))
                break
        else:
            print("列表中不存在该员工姓名！")
        name=input("请输入您要删除信息的员工姓名：")
    print("程序结束！")

def sy12():
    lst_odd=[1,3,5,7,9]
    lst_even=[2,4,6,8,10]
    #2列表拼接
    lst_odd.extend(lst_even)
    lst_odd.sort(reverse=True)
    print(lst_odd)

def sy13():
    s = input("请输入一段英文：")
    s = s.lower()
    lst = []
    for c in s:
        if c.isalpha():
            if c not in lst:
                lst.append(c)
    lst.sort()
    print(lst)
def sy14():
    a=range (10, 100)
    lst=random.sample(a, 20)
    lst1=sorted(lst[:10])
    lst[:10]=lst1
    lst2=sorted(lst[10:],reverse=True)
    lst[10:]=lst2
    print(lst)
def sy15():
    def sentence_reverse(s):
        lst = s.split(" ")
        return " ".join(lst[::-1])

    s1 = input("请输入一段英文：")
    s2 = sentence_reverse(s1)
    print(s2)

def sy16_1():
    lst_floor = [1, 4, 2, 5, 7, 3]
    for i in range(1, len(lst_floor)):
        end = lst_floor[i]
        start = lst_floor[i - 1]
        if start < end:
            print("↑" * (end - start), end="")
        else:
            print("↓" * (start - end), end="")
def sy16_2():
    route = "↑↑↓↓↓↑↑↓↓↑↑↑"
    lst_floor = [2]
    floor = 2
    for ch in route:
        if ch == "↑":
            floor += 1
        else:
            floor -= 1
        lst_floor.append(floor)
    print(",".join([str(x) for x in lst_floor]))
def sy18():
    s = "语文:80,数学:82,英语:90,物理:85,化学:88,美术:80"
    lst_score = []
    for x in s.split(","):
        i = x.index(":") + 1
        score = int(x[i:])
        lst_score.append(score)

    zf = sum(lst_score)
    print("总分：{} 平均分：{:.1f}".format(zf, zf / len(lst_score)))