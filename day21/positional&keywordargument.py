#A positional argument is an argument passed to a function based on the order in which the parameters are defined
#Values are passed according to their position/order
def student(name, age):
    print(name)
    print(age)

student("Sowbhagya", 21)#"Sowbhagya" → name because it is in 1st position
                        #21 → age because it is in 2nd position


#A keyword argument is an argument passed to a function by explicitly specifying the parameter name.
#Values are passed using the parameter name.
def student(name, age):
    print(name)
    print(age)

student(age=21, name="Sowbhagya")#order is changed,python knows which value belongs to which parameter because of parameter names.


#we combine postional with keyword arguments.
#RULE:But positional arguments must come before keyword arguments.
def student(name, age, city):
    print(name, age, city)

student("Sowbhagya", age=21, city="Hyderabad")

#Duplicate argument X 
#Don't give the same parameter twice.
def student(name, age):
    print(name, age)

student("Sowbhagya", name="Laxmi")
#name gets two values, so Python raises an error.


#Missing argument X
def student(name, age):
    print(name, age)

student("Sowbhagya")
#age is missing, so Python raises a TypeError.