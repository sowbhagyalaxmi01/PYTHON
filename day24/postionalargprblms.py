#Order Changes Everything
def calculate(a, b, c):
    return a * 100 + b * 10 + c

print(calculate(2, 5, 7))
print(calculate(7, 5, 2))


#Same Values, Different Positions
def operation(a, b, c):
    return a - b * c

print(operation(20, 3, 2))
print(operation(3, 20, 2))
print(operation(2, 3, 20))

#Four Parameters
def display(a, b, c, d):
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("d =", d)

display(40, 10, 30, 20)


#Function Calling Function
def add(a, b):
    return a + b

def calculate(x, y):
    return add(y, x) * 2

print(calculate(10, 20))


#Positional Arguments + Returned Values
def numbers(a, b, c):
    return c, a, b

x, y, z = numbers(10, 20, 30)

print(x)
print(y)
print(z)

#Nested Function Calls
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(multiply(add(2, 3), add(4, 5)))


#Same Function, Different Calls
def result(a, b, c):
    return a * b + c

x = result(2, 3, 4)
y = result(4, 3, 2)
z = result(3, 4, 2)

print(x, y, z)

#Too Few Arguments(error)
def student(name, age, branch, year):#Required parameters = 4
 print(name, age, branch, year)#Given arguments = 3

student("Ravi", 21, "AIML")

#Too Many Arguments(error)
def student(name, age):
    print(name, age)

student("Ravi", 21, "AIML")#paramters 2 and arguments 3

#Difficult Mapping
def test(a, b, c, d):
    return a + b * c - d

print(test(5, 2, 3, 4))
print(test(2, 5, 4, 3))