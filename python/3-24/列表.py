# gucsts = ['小冯','小李','小王','小赵']
# m = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# print(m[9-1])
# gucsts.append('小孙')
# gucsts.insert(0,'小二')
# gucsts.pop(3)
# gucsts.remove('小李')
# for i in gucsts:
#     print(f"欢迎{i}")
# for i in range(len(gucsts)):
#     print(f"{i+1}是{gucsts[i]}")
# print(gucsts)
# print(range(len(gucsts)))
film=[["哪吒之魔童降世",50],["流浪地球", 46],["我和我的祖国", 31],["中国机长",29],["疯狂的外星人", 22]]
mun = 0
i = 0
for m in film:
    i += 1
    mun += m[1]
    print(f"No.{i}\t{m[0]}\t{m[1]}")
print(f"总票数：{mun}")