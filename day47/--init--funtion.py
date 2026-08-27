# __init__ is constructor which is automatically called an object is created. it is used to intialixe the objects attributes
class Student:
    def __init__(self):
        print("Student object created")
s1 = Student()#when this line runs python automatically calls __init__()


# why do we use __init__()?
# We mainly use __init__() to initialize (set) the object's data.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Keerthi", 20)

print(s1.name)
print(s1.age)
# self.name = name and self.age = age  both stores the values inside object


#__init__() without parameter
class Car:
    def __init__(self):
        self.brand = "BMW"
        self.speed = 100
c1 = Car()
print(c1.brand)
print(c1.speed)

#Default values
class Student:
    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age

s1 = Student()
print(s1.name)
print(s1.age)

#Why do we need __init__()?
#Because we want different objects to have different data.
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Keerthi")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)


#__init__() with a method
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

s1 = Student("Keerthi", 20)

s1.display()
#__init__() → initializes data
# display() → performs an action
# self → refers to the current objec


#self means the current object.
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Keerthi")
# s1 → object
# self.name = name
# self means s1.
# So Python is basically doing:
# s1.name = "Keerthi"