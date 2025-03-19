def isOdd(n): #3
    if n%2==0:
        return False
    else:
        return True
    
def sy4(x):
    while x <= 500:
        x = 5 * x + 1
    return x

def sy5(n,y):
    out = (n * 2 + 5)* 50 + 1766 - y
    out = out % 100
    return out
import random
def honbao12(m=100,n=15):
    out = []
    for i in range(n):
        # temp = round(random.uniform(0.01,m-((n-1-i)*0.01)),2)
        temp = round(random.uniform(0.01,m/n*2),2)
        m -= temp
        out.append(temp)
    return out

def isdiff(n): #13
    st = str(n)
    for i in range(len(st)-1):
        if st[i] != st[i+1]:
            return 1
    return 0

def judge(password):  #14
    fen1,fen2,fen3,fen4 = 0,0,0,0
    password = str(password)
    lenth = len(password)
    if lenth >= 8: fen4 = 1
    for i in range(lenth):
        if '0' <=password[i] <= '9':
            fen1 = 1
            continue
        if 'a' <=password[i] <= 'z':
            fen2 = 1
            continue
        if 'A' <=password[i] <= 'Z':
            fen3 = 1
            continue
    return fen1+fen2+fen3+fen4

def fen(n): #17
    out = 0
    for i in range(1,n+1):
        out += 1/i
    return out

def fen2(n): #17
    if n == 1:
        return 1
    else:
        return 1/n + fen2(n-1)
def gwsh(n): #求各个位数之和
    num = 0
    while n > 0:
        num += n%10
        n //= 10
    return num
def sy8():
    out = []
    for i in range(100,1000):
        if gwsh(i * 3) == gwsh(i*4) == gwsh(i * 5) == gwsh(i*6) == gwsh(i*7):
            out.append(i)
    return out
def sy9(n):
    out = 0
    for i in range(1,n):
        if n % i == 0:
            out += i
    if out == n:
        return 1
    else:
        return 0