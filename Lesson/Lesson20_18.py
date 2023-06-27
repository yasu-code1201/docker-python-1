def info(func):
    def wrapper(*args, **kwargs):#args:可変長位置引数　kwargs:可変長キーワード引数
        print("Start!!")
        func(*args, **kwargs)
        print("Finish!!")
    return wrapper

@info
def add(a, b):
    print(a + b)
    
@info
def add2(c, d, e):
    print(c + d + e)

add(1, 2)
add2(3, 4, 5)
    