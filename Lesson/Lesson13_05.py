class Student:
    def avg(self,math,english):#メソッドの引数には、どんな場合でも self と書く
        print((math + english)/2)
        
a001 = Student()#クラスを使えるような状態にすることを「インスタンス化」「オブジェクト化」「オブジェクト生成」　インスタンス化とは、クラスという型からインスタンスと言う実際に使える「モノ」を作る
a001.avg(30,70)

a001.name = "sato"
print(a001.name)

print(a001.gender)