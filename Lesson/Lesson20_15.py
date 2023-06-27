def circle_area(pi):
    def calculacion(radius):  #クロージャー:calculacion
        return pi * radius * radius
    return calculacion

area1 = circle_area(3.14) #pi
area2 = circle_area(3)    #pi

print(area1(2))  #radius
print(area2(2))  #radius 