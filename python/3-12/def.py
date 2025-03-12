def find_str(text,ssw):
    res = text.find(ssw)
    if res != -1:
        stars = len(ssw) * '*'
        text = text.replace(ssw,stars)
        print('end:'+text)
    else:
        print('no')
def finding():
    text = '特用户1：衣服质量与描述完全不符，真的不知道评价里面的好评是' \
        '怎么来的？！买的蓝色到手的是黑色，衣服刺鼻味超级严重，衣领没什么型，' \
        '衣服上的横纹是印刷上去的，特么的还掉色，不是针织、不是纯棉，' \
        '是尼龙或者更差的布料，透气性很差，穿着还不舒服。' \
        '这是网购以来最差的衣服，特么的差评。'
    ssw = '特么的'
    find_str(text,ssw)