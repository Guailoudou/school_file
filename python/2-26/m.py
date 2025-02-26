# num = input("in")
# num = "420116200409038516"
# put = num[6:10]+"年"+num[10:12]+"月"+num[12:14]+"年"
# print(put)

num = input("in：")
put = num[0:2]+num[4]
print(put)

xx = "*"*5+"\n"
print(xx*5)
"*" in xx #true

s="李白说：大鹏一日同风起，扶摇直上九万里。常建说：恐逢故里莺花笑，\
且向长安度一春。杜甫说：会当凌绝顶，一览众山小。高适说：二十解书剑，\
西游长安城。"
print(s.find("长安"))
print(s.rfind("长安"))
print(s.find("2"))\

# s="燕子去了，有再来地时候；杨柳枯了，有再青地时候；桃花谢了，有再开地时候。"
# m= s.replace("地","的")
# print(m)

s="长-安-三-万%里"
m=s.replace("-","").replace("%","")
print(m)