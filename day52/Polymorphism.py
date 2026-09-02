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



#    