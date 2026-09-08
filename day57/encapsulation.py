#Encapsulation----------------

# Encapsulation means wrapping data and methods into a single unit and
# restricting direct access to data
#__variablename = private var
"""
class student:
    def __init__(self):

        self.name = "Ram"
        self.marks = 80

s = student()
print(s.name)
print(s.marks)
"""
#private var access---
"""
class student:
    def __init__(self):

        self.name = "Ram"
        self.__marks = 80
    
    def get_marks(self):
        return self.__marks
    
        

s = student()
print(s.name)
print(s.get_marks())
"""

#private var---

"""
class Employ:

    def __init__(self):
        self.__sal = 50000

    def get_sal(self):
        return self.__sal

    def set_sal(self,sal):
        self.__sal = sal

e= Employ()
print(e.get_sal())#first sal before changing

e.set_sal(70000) #change sal

print(e.get_sal()) #sal after change
"""

#protect vaar

class Example:
    def __init__(self):
        self.name = "public"
        self._age = 22
        self.__sal = 50000

    def sal_get(self):
        return self.__sal
    def sal_mod(self, sal):
        self.__sal = sal
    def set_age(self,age):
        self._age = age
    def get_age(self):
        return self._age
class ch1(Example):

    def display(self):
        print("age:", self._age)#if the var contains _varname: protected parameter
        print("sal:", self.__sal)
    

e = Example()
c = ch1()

#print(c.display())

print(e.name) #public
print(e._age) #protected val-22
e.set_age(18) #changing the protected val-18
print(e.get_age())# get the changed age-18
print(e.sal_get()) #get the changed sal-50000
print(c.sal_get())

# when we are working with private and protected parameters
#we can modify & access them using set and get methods but whenever
# we are working with sub classes we can only access protected parameters but not private parameters---