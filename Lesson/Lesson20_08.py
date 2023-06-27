def show_number(a,  b, *args): #*args:可変長位置引数
    print(a)
    print(b)
    for i in args:
        print(i)
    
show_number(1, 2, 3, 4, 5)
    