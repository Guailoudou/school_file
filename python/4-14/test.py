# py
sns = ['松饼','提拉米苏','芝士蛋糕','三明治']
drs = ['红茶','咖啡','橙汁']

# ms = []
# for sn in sns:
#     for dr in drs:
#         m = (sn,dr)
#         ms.append(m)

# ms = [(sn,dr) for sn in sns for dr in drs]
# ms = []
# for sn in range(len(sns)):
#     for dr in range(len(drs)):
#         m = (sns[sn],drs[dr])
#         ms.append(m)

# for m in ms:
#     print(m)

first_idiom = '万事如意'
end_str = first_idiom[-1] 
new_li = [first_idiom]
li = ['发愤图强', '笑容满面', '意气风发', '强颜欢笑'] 
for index in range(len(li)):
    for i in li:
        if end_str == i[0]: 
            new_li.append(i) 
            li.remove(i) 
            end_str = i[-1] 
            break
print(new_li)