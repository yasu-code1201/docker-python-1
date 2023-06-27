def outer_func(a,b): #関数内関数　outer:外側
    def inner_func(c,d): #関数内関数　inner:内側
        return c - d # 2 - 1 =1=x

    x = inner_func(2,1) # c=2 d=1 
    y = inner_func(a,b) # c = a  d = b : c=3 d=1 : 3-1=2 
    print(x)
    print(y)

outer_func(3,1) # a=3 b=1