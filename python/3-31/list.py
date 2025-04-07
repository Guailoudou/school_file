
# ll = [i**2 for i in range(10) if i%2==0]
# print(ll)
# values=[['萧峰',114],['杨过',110],['令狐冲',95],['张无忌',106],['郭靖',113]]
# l2 = [i[0] for i in values if i[1]>100]
# print(l2)
# tables = [['萧峰',20,17,20,20,18,19],
#           ['杨过',18,19,17,20,18,18],
#           ['令狐冲',12,17,14,20,19,13],
#           ['张无忌',20,17,15,14,20,20],
#           ['郭靖',19,18,19,18,19,20]]
# l3 = [(item[0],sum(item[1:])) for item in tables]
# for i in range(1,7):
#     print(f"{sum([item[i] for item in tables])/5:.2f}")
# print(l3)

l = [54,36,75,28,50]
l.append(42)
print(l)
l.insert(l.index(28),66)
print(l)
l.remove(28)
print(l)
l.sort(reverse=True)
print(l)
l.clear()
print(l)