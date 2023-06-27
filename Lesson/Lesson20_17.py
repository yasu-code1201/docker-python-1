def info(func):
    def wrapper(a, b):
        print("Start!!")
        func(a, b)
        print("Finish!!")
    return wrapper

def add(a, b):
    print(a + b)
    
    
add_result = info(add)
add_result(1, 2)
add_result(3, 4)