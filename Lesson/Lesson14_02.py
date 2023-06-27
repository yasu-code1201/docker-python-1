class Student:
    
    def __init__(self,name):
        self.name = name # selfを書くことにより、selfにインスタンスが代入される
    
    def calculate_avg(self,data):
        sum = 0
        
        for num in data:
            sum += num
            
        avg = sum/len(data)
        return avg
    
    def jedge(self,avg):
        
        if(avg >= 60):
            resalt = "passed"
        else:
            resalt = "failed"
        return resalt

a001 = Student("sato")
data = [70,65,50,10,30]
avg = a001.calculate_avg(data)
resalt = a001.jedge(avg)

print(avg)
print(a001.name + " " + resalt)