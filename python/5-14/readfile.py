import os
import csv
# os.chdir(r"C:\Users\Administrator\Desktop")

print(os.getcwd())
file=open("123.txt","w")
file.write("114515\n11451\t114")
file=open("123.txt","a")
ls = ["\nweqeq\n","23esd"]
file.writelines(ls)
file=open("123.txt","r")
print(file.read())
file.close()

with open("stu.csv","a",newline='') as stcsv:
    writer = csv.writer(stcsv)
    writer.writerow(['qw','n','2'])
    writer.writerows([['qw', 'n', '2'],['qwq', 'n', 'm']])

with open("stu.csv","r") as stcsv:
    reader = csv.reader(stcsv)
    for r in reader:
        print(r)
        
try:
    a=int(input("a="))
    b=int(input("b="))
    c=a/b
except ZeroDivisionError:
    print("/0?")
else:
    print("c=",c)