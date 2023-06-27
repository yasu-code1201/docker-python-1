class Student:
    
    def __init__(self):
        self.name = "" # selfを書くことにより、selfにインスタンスが代入される
    
    
    def avg(self,math,english):
        print((math + english)/2)
        
a001 = Student()

a001.name = "sato"
print(a001.name)

a002 = Student()
a002.name = "tanaka"
print(a002.name)