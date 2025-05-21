def test3(x,*t):
    print("x:",type(x),":",x)
    print("t:",type(t),":",t,"len:",len(t))
list = [1,2,3,4,5]
test3(1,list)