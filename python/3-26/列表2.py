film=[["哪吒之魔童降世",50.01],["流浪地球", 26.79],["我和我的祖国", 31.19],["中国机长",29.00],["疯狂的外星人", 22.11]]
# num = 0
# a = []
# for i in range(len(film)):
#     print(f"No.{i} \t {film[i][0]: <7} \t {film[i][1]}")
#     num += film[i][1]
#     a.append(film[i][1])
# print(f"总：{num:.2f} or {sum(a):.2f}")

def f(x,y):
    if x[1]>y[1]:
        return x[1]
    return y[1]
list = [10,3,3,4,3,6,7,8,3,10]
print(sorted(list,reverse=True))
print(sorted(film,key = lambda x:x[1],reverse=True))
film1 = film
film2 = film.copy()
del film1[0]
print(film)
print(film1)
print(film2)
# print(film.sort(film,lambda x:x[1],reverse=True))