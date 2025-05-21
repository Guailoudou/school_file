dicGDP={'2022 年': 1210207.2, '2021 年': 1149237.0, '2020 年': 1013567.0}
dicGDP.clear()
st = "asdasdada"
cou = {}
st = st.lower()
for i in st:
    cou[i] = cou.get(i,0) + 1
    if i in cou:
        cou[i] += 1
    else:
        cou[i] = 1

dicAreas = {'俄罗斯': 1707.5, '加拿大': 997.1, '中国': 960.1} 
m = 0
for key in dicAreas.keys():
    print(key, dicAreas[key])
for k,v in dicAreas.items():
    print(k,v)
    m+=v
print(m)