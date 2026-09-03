#Class + Object
class Student:
    name = "Rahul"
    age = 20
s1=Student()    
print(s1.name) 
print(s1.age)   


#Create a Car class with brand and model.
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
p1=Car("Toyota", "Camry")
print(p1.brand)
print(p1.model)   


#Create an Employee class with name and salary.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e1 = Employee("John", 50000)
print(e1.name)
print(e1.salary)


#Create a Book class using __init__() with:title,author
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
b1 = Book("Python Basics", "John")
print(b1.title)
print(b1.author)


#Create a Mobile class using __init__() with:brand,price,Create two objects.
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
m1 = mobile("Apple", 60000)
m2 = mobile("Samsung", 50000)
print(m1.brand)
print(m1.price)
print(m2.brand)
print(m2.price)


#Attributes + self Create a Person class with:name,age and create a method.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
       print(f"My name is {self.name} and I am {self.age} years old.") 
p1=Person("sowbhagya",20)
p1.introduce()   


#Q7. Create a Rectangle class with:length,width and Create a method:area()
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length * self.width)
r1=Rectangle(20,60)
r1.area()    


#Student Marks and Create a Student class with:name,maths,science and Create a method:total()
class Marks:
    def __init__(self,name,maths,science):
        self.name=name
        self.maths=maths
        self.science=science
    def total(self):
         print(self.maths + self.science)# print(f"{self.name}: {self.maths + self.science}") inlcuding name
t1=Marks("varun",60,80)
t1.total()            


#Q9. Dog and Create a Dog class with:name,breed and Create a method:bark()
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking {self.breed}")

b1 = Dog("Tommy", "Labrador")
b1.bark()

#Create a Calculator class. Create methods:add(a, b),subtract(a, b),multiply(a, b),divide(a, b)
class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
c = Calculator()
print(c.add(10, 5))
print(c.subtract(10, 5))
print(c.multiply(10, 5))
print(c.divide(10, 5))
#by using __init__
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
c = Calculator(10, 5)
print(c.add())
print(c.subtract())
print(c.multiply())
print(c.divide())