import random
import os
def getyzm():
    list="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    yzm = ''
    for i in range(6):
        yzm+=list[int(random.random()*len(list))]
    return yzm

def getyzm2():
    code_list = ''
    for i in range(6):
        state = random.randint(1,3)
        if state == 1:
            code_list += chr(random.randint(48,57)) #数字
        elif state == 2:
            code_list += chr(random.randint(65,90)) #大写字母
        else:
            code_list += chr(random.randint(97,122)) #小写字母
    return code_list

# h = 0
# while True:
#     if getyzm() == "KFCV50":
#         print("KFCV50!!!!")
#         break
#     else:
#         h+=1
#         os.system('cls')
#         print(h)

def st(count):
    ball = ""
    for i in range(count):
        white = random.sample(range(1,60), 5)
        for item in white:
            ball += str(item).zfill(2)+" "
        red = random.sample(range(1,36), 1)
        ball += str(red).zfill(2)+"\n"
    print(ball)
count = int(input("："))
st(count)