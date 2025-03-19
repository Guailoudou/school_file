def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
# num = 0
# for i in range(1,20+1):
#     num += fibo(i)
# print(num)
        # print("{:>8}".format(fibo(i)),end=" " if i%5!=0 else "\n")

f = lambda x: x<0
list = [1,2,3,-4,5,-6,7,8,9,10]
for i in filter(f,list):
    print(i)
print(list)
