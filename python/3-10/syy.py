import random

list=["春暖花开","十字路口","千军万马","白手起家","张灯结彩","风和日丽","万里长城","人来人往",
    "自由自在","瓜田李下","助人为乐","白手起家","红男绿女","春风化雨","马到成功","拔苗助长","安居乐业",
    "走马观花","念念不忘","落花流水","张灯结彩","一往无前","落地生根","天罗地网","东山再起","一事无成",
    "山清水秀","别有洞天","语重心长","水深火热","鸟语花香","自以为是"]

def one(list):
    w = random.choice(list)
    bank = random.randint(0,len(w)-1)
    new = w[:bank] + "__" + w[bank+1:]
    print(new)
    put = input("请输入：")
    if put.strip(" ") == w[bank]:
        print("恭喜你猜对了")
        return 2
    elif not put:
        print("过")
        return 0
    elif put != w[bank]:
        print("错了,答案是：",w)
        return -2
def cai():#猜数字游戏
    num = 20
    for i in range(8):
        num += one(list)
    print("你",num,"分")
def sy1():
    num = 0
    for i in range(1,11):
        num *= i
    print(num)
def sy2():
    num = 0
    for i in range(1,100,2):
        num += i
    print(num)
def sy3():
    #num = 0
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

def sy8():
    num = 0
    for i in range(1,101,3):
        temp = 0
        for j in range(i,i+3):
            temp *= j
        num += temp
    print(num)
    
def sy10():
    n = random.randint(0,9)
    print(n)
    while True:
        inp = input("请输入：")
        ii = int(inp)
        if ii == n:
            print("恭喜你猜对了")
            break
        elif ii > n:
            print("大了")
            continue
        elif ii < n:
            print("小了")
            continue
def sy12():
    num = 0
    for i in range(100):
        num += random.randint(0,1)
    print("0="+str(100-num),"1="+str(num))

def sy13():
    wli = 1
    for i in range(365):
        for j in range(5):
            wli = wli + (wli * 0.01)
        for n in range(2):
            wli = wli - (wli * 0.01)
    print(wli)
def hlm(): #红楼梦题词统计
    str = """
    怪奴底事倍伤神？半为怜春半恼春。怜春忽至恼忽去，至又无言去不闻。
    昨宵庭外悲歌发，知是花魂与鸟魂？花魂鸟魂总难留，鸟自无言花自羞；
    愿奴胁下生双翼，随花飞到天尽头。天尽头，何处有香丘？
    未若锦囊收艳骨，一抔净土掩风流；质本洁来还洁去，强于污淖陷渠沟。
    尔今死去侬收葬，未卜侬身何日丧？侬今葬花人笑痴，他年葬侬知是谁？
    试看春残花渐落，便是红颜老死时。一朝春尽红颜老，花落人亡两不知！
    """
    s1="为"
    s2="以"
    s3="何"
    r1 = str.count(s1)
    r2 = str.count(s2)
    r3 = str.count(s3)
    rr = "词:{:-^5} 出现了：{:-^5} 次"
    print(rr.format(s1,r1))
    print(rr.format(s2,r2))
    print(rr.format(s3,r3))

def bfe(): #波菲尔数列前n和
    put=input("请输入：")
    iput = int(put)
    num = 2
    n1 = 1
    n2 = 1
    if iput == 1:
        print(1)
        return
    if iput == 2:
        print(2)
        return
    for i in range(iput-2):
        temp = n1 + n2
        n1 = n2
        n2 = temp
        num += temp
    print(num)
bfe()