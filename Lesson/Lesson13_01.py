class Student:
    def avg(self):#メソッドの引数には、どんな場合でも self と書く
        print((80+70)/2)
        
a001 = Student()#クラスを使えるような状態にすることを「インスタンス化」「オブジェクト化」「オブジェクト生成」　インスタンス化とは、クラスという型からインスタンスと言う実際に使える「モノ」を作る
a001.avg()
