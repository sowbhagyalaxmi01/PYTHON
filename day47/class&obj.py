class student:
    name="kushi"
s1=student()   
print(s1.name) 
s2=student()
print(s2.name)


#factors making cars
class car:
    color="blue"
    brand="audi"

car1=car()
print(car1.color)  
print(car1.brand)  

#multiple objects
class rest:
    x=9
p1=rest()
p2=rest()
p3=rest()
print(p1.x)
print(p2.x)
print(p3.x)    

#delete of object using del
class myclass:
    x=3
p1=myclass()
del p1
print(p1.x)  #we will get error becoz p1 was deleted  