# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)
def forin():
    num="296049623434251586137447705397389574602496296804807004337087"
    order=""
    for i in range(10):
        count = num.count(str(i))
        order += str(i) + ":" + str(count) + "\n"


def forelse():
    n = int(input("请输入一个正整数："))
    for i in range(2, n):
        if n % i == 0:
            print(n, "不是素数")
            break
    else:                     # 循环结束后执行,break后不执行
        print(n, "是素数")

import random
def dubo():
    money = 10
    max = money
    while money >0:
        num1 = random.randint(1,6)
        num2 = random.randint(1, 6)
        if num1 + num2 ==7:
            money += 4
            if money > max: max = money
        else:
            money -= 1
        print(money,end='  ')
    print("\nmax",max)



if __name__ == '__main__':
    dubo()