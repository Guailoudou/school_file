lunar = '申酉戌亥子丑寅卯辰巳午未'
zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = input('请输入要查询属相的年份:')

# if rem == 0:
#     print('属相为',zodiac[11],'年')
#     p2004rint('属相为',lunar[11],'年')
# else:

if year.isdigit():
    rem = int(year) % 12
    print('：',zodiac[rem],lunar[rem])
else:
    print('err')