def show_number(**kwargs): #可変長キーワード引数
    print(kwargs)
    
d = {"a": 1, "b": 2, "c": 3}
    
show_number(**d)