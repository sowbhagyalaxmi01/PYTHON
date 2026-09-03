#Polymorphism means “many forms.”
# In Python, it means the same method/function name can behave differently depending on the object.
#Simple real-life example
# Think about the word “speak”:
# Dog → barks
# Cat → meows
# Human → talks
# Same action: speak
# Different behavior: depending on the object


class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")
d = Dog()
c = Cat()
d.speak()
c.speak()



#why we need polymorphism?
#We need polymorphism to allow the same method or interface to work with different objects, reducing conditional code and making programs more reusable, flexible, and maintainable.
# Code reuse – one function works for many objects.
# Less code – reduces unnecessary if-else.
# Flexibility – easily add new classes.
# Easy maintenance – changes are easier to manage.
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


class Cow:
    def sound(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()


#types/forms of polymorphism(3)
#1.method overridding
# Parent and child have the same method, but the child gives a different implementation.
#Key: inheritance is required.
class Animal:
    def sound(self):
        print("Animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


d = Dog()
d.sound()


#2.Method Overloading
# Same method name with different arguments.
# Python does not support traditional method overloading like Java/C++.
# We usually achieve similar behavior using default arguments:
#Key: same method, different number of arguments.
class Calculator:
    def add(self, a, b, c=0):
        print(a + b + c)

c = Calculator()
c.add(10, 20)
c.add(10, 20, 30)


#3.Duck Typing
#Python doesn't care about the object's class. It cares whether the object has the required method.
class Dog:
    def sound(self):
        print("Bark")


class Cat:
    def sound(self):
        print("Meow")


def make_sound(animal):
    animal.sound()


make_sound(Dog())
make_sound(Cat())