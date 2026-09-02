#inheritance---- one class gets properties & methods from another class


"""
class basecar: #parent class
    def basic(self):
        print("Basic model")

        
class car(basecar): #childclass
    def maincar(self):
        print("black car")

c1 = car()
c1.basic()
#c1.maincar()
"""


class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    print("Hiiiiiiiiii")
    def sk(self):
        print("dog is speaking")

d = Dog()
d.speak()
d.sk()

#parent class- Employee-method, child class developer-method- create obj for developer class 
#with the help of it access the parent class method


#types of Inheritance-----
"""
1. Single Inheritance: one parent -> one child
2. Multiple Inheritance: multiple parent -> one child
3. Multilevel Inheritance: cl -> cl1 -> cl2 : grandpa -> parent -> child
4. Hierarchical Inheritance: one parent -> multiple child
"""


#multiple inheritance------

class A:
    def aa(self):
        print("class  A")

class B:
    def bb(self):
        print("class B")

class C(A,B):
    print("Hiiiiiiiiiiiiiiiiiiii")
    def cc(self):
        print("class C")



objc = C() #child


objc.aa()
objc.bb()
objc.cc()


#multilevel inheritance-----


class A: #grand parent
    def aa(self):
        print("class  A")

class B(A): #parent
    def bb(self):
        print("class B")

class C(B): #child
    def cc(self):
        print("class C")


b = B()
b.aa()
c = C()
c.bb()
c.aa()

# Hierarchical Inheritance-----------

"""
class A:
    def aa(self):
        print("class  A")
    
    def kk(self):
        print("it's for C")
    
class B(A):
    def bb(self):
        print("class B")

class C(A):
    def cc(self):
        print("class C")


b = B()
c = C()

b.aa()
c.kk()
b.bb()
"""

"""
class vehicle:
    def __init__(self,name):
        self.name = name

class bus(vehicle):
    def __init__(self, name,color):
        super().__init__(name)
        self.color = color

b = bus("dog","black")
print(b.name, b.color)      
"""


# super() key word in Inheritance-----
# even though we are passing the parent class name into the child class , when the
#child class contains constructor , it will only print it's own attributes and
#properties & couldn't access the data from parent class 


"""
class Car:
    def __init__(self, name):
        self.name = name
        #self.age = age

class red_c(Car):
    def __init__(self, color, name):
        super().__init__(name)
        self.color = color

    

c = red_c("blue", "ram")
print(c.color, c.name)

"""



"""
class Car:
    def __init__(self, name):
        self.name = name
        #self.age = age

class red_c(Car):
    def details(self):
        print("Hi my name is", self.name)

    

c = red_c(name="Ram")
c.details()

"""