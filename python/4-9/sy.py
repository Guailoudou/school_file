def sy19():
    first = [
        ("triangle", "shape"),
        ("red", "color"),
        ("square", "shape"),
        ("yellow", "color"),
        ("green", "color"),
        ("circle", "shape")
    ]
    first_new = [[x, x] for x in first]
    first_sort = sorted(first_new)
    first_colors = [x for x in first_sort if x == "color"]
    print("按照标签排序后的列表：{}".format(first_sort))
    print("颜色列表：{}".format(first_colors))
def sy20():
    import random
    lst_suit = ["黑桃", "红桃", "梅花", "方块"]
    lst_face = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
    lst = [y + x for x in lst_face for y in lst_suit]
    random.shuffle(lst)
    idx_user = int(input("请您抽一张牌（0~51）："))
    card_user = lst[idx_user]
    print("您抽到的牌是：{}".format(card_user))
    remaining_indices = [i for i in range(52) if i != idx_user]
    idx_computer = random.choice(remaining_indices)
    card_computer = lst[idx_computer]
    print("电脑抽到的牌是：{}".format(card_computer))
    val_user = lst_face.index(card_user[2:].strip())
    val_computer = lst_face.index(card_computer[2:].strip())
    if val_user > val_computer:
        print("恭喜，您赢了！")
    elif val_user < val_computer:
        print("很遗憾，您输了！")
    else:
        print("咱们平手了！")

def sy21():
    lst_score = [9, 10, 8, 9, 10, 7, 6, 8, 7, 8]
    lst_score.sort() 
    lst_score.pop()  
    lst_score.pop(0) 
    average = sum(lst_score) / len(lst_score)
    print("该选手的最终得分为：{}".format(average))

def sy22():
    lst_weather = [
        ["周一", "16℃", "26℃", "多云", "1级", "优"],
        ["周二", "17℃", "27℃", "晴", "2级", "优"],
        ["周三", "16℃", "28℃", "晴", "3级", "优"],
        ["周四", "16℃", "25℃", "阴", "2级", "良"],
        ["周五", "15℃", "24℃", "阴", "2级", "良"],
        ["周六", "15℃", "25℃", "晴", "3级", "优"],
        ["周日", "14℃", "23℃", "小雨", "3级", "良"]
    ]
    # 1. 空气质量为优的天数
    number_condition1 = [x[0] for x in lst_weather if x[5] == "优"]
    print("空气质量为优的天数：{}，它们分别是：{}".format(len(number_condition1), ",".join(number_condition1)))
    # 2. 风力低于3级且最高气温≤25℃的天数
    number_condition2 = [x[0] for x in lst_weather if (int(x[2][:-1]) <= 25 and int(x[4][:-1]) < 3)]
    
    print("风力低于3级且最高气温不超过25℃的天数：{}，它们分别是：{}".format(len(number_condition2), ",".join(number_condition2)))
    # 3. 平均气温低于20℃的天数
    number_condition3 = [x[0] for x in lst_weather if (int(x[1][:-1]) + int(x[2][:-1])) / 2 < 20]
    print("平均气温低于20℃的天数：{}，它们分别是：{}".format(len(number_condition3), ",".join(number_condition3)))

def sy23():
    n = 300
    lst_prime = []
    for i in range(2, n + 1):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(i)
    print("{0}以内素数有：{1}".format(n, ",".join(map(str, lst_prime))))

sy23()
