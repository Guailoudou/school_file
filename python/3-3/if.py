# str = "明月晓啼莺，莺啼晓月明"
# if str == str[::-1]:
#     print("回文")
# else:
#     print("非回文")

# print("回文") if str == str[::-1] else print("非回文")
import random
def random_num():
    a = random.randint(101,501)
    b = random.randint(101,501)
    return a,b

def co(a,b,n):
    rn = n[::-1]
    print("中奖号码为：",a,b)
    if a == int(n) or b == int(n):
        print("一等奖")
        return 1
    elif a == int(rn) or b == int(rn):
        print("二等奖")
        return 2
    elif a%10 == int(n)%10 or b%10 == int(n)%10:
        print("三等奖")
        return 3
    else:
        print("无奖")
        return 0

if __name__ == '__main__':
    j1,j2,j3,j0 = 0,0,0,0
    for i in range(20000):
        a,b = random_num()
        # a,b = 101,102
        
        # n = 106
        n = random.randint(101,501)
        # n = input(":")
        # if n.isdigit() == False or int(n) > 500 or int(n) < 101:
        #     print("非法输入")
        #     exit(0)
        o = co(a,b,str(n))
        if o == 1:
            j1 += 1
        elif o == 2:
            j2 += 1
        elif o == 3:
            j3 += 1
        else:
            j0 += 1
    print("一等奖：",j1,"二等奖：",j2,"三等奖：",j3,"无奖：",j0)

    

