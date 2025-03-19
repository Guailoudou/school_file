
def finding():
    text = '特用户1：衣服质量与描述完全不符，真的不知道评价里面的好评是' \
        '怎么来的？！买的蓝色到手的是黑色，衣服刺鼻味超级严重，衣领没什么型，' \
        '衣服上的横纹是印刷上去的，特么的还掉色，不是针织、不是纯棉，' \
        '是尼龙或者更差的布料，透气性很差，穿着还不舒服。' \
        '这是网购以来最差的衣服，特么的差评。'
    ssw = '特么的'
    find_str(text,ssw,len(ssw) * '*')

def cSUM(n1,n2):
    sum = 0
    for i in range(n1,n2+1):
        sum += i
    return sum

def isss(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def lsss(): #找到2-100的孪生素数
    for i in range(2,101):
        if isss(i) and isss(i+2):
            print(i,i+2)
            
def return_t(a,b):
    return a,b

def find_str(text,ssw,re):
    res = text.find(ssw)
    if res != -1:
        text = text.replace(ssw,re)
        print('end:'+text)
    else:
        print('no')


if __name__ == '__main__':
    text = '我们拥有多年的品牌战略规划及标志设计、商标注册经验；专业提供公司标志设计与商标注册一条龙服务。我们拥有最优秀且具有远见卓识的设计师，使我们的策略分析严谨，设计充满创意。我们有信心为您缔造最优秀的品牌形象设计服务，将您的企业包装得更富价值。'
    find_str(text,'最优秀','较优秀')