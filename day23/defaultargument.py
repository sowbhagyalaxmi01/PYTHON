#Default argument means: a parameter already has a value, and Python uses that value if you don't provide one when calling the function.
#default is the value written inside the function definition.
def greet(name, message="Hello"):
    print(message, name)

greet("Ravi")
#name → no default
#message → default is "Hello"
#"Ravi" is the argument we gave to name.
#message was not given, so Python uses its default:


## Q2. Create a function student(name, age=18).
# If age is not provided, use 18.
def student(name,age=18):
    print(name,age)
student("Rakesh")
student("sita",21)

# Q3. Create a function that takes name and country.
# Set "India" as the default country.
def country(name,country="India"):
    print(name,country)
country("sita")
country("suresh","Germany")    


#Multiple Default Parameters
def student(name,age=20,branch="CSM"):
    print(name,age,branch)
student("RAVI")   


#Change One Default
def student(name, age=21, branch="CSE"):
    print(name, age, branch)
student("Ravi", 22)


#Skip a Default Using Keyword(default+keyword)
def student(name, age=21, branch="CSE"):
    print(name, age, branch)
student("Ravi", branch="AIML")


#Predict the Output
def calculate(a, b=10):
    return a + b

print(calculate(5))
print(calculate(5, 20))

#power
def power(a, b=2):
    return a ** b

print(power(5))
print(power(5, 3))

#default and keyword
def employee(name, salary=30000, role="Developer"):
    print(name, salary, role)

employee("Ravi", role="Tester")


#Calculator
def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b

print(calculator(10, 5))
print(calculator(10, 5, "sub"))


#Rectangle
def rectangle(length, width=10):
    return length * width

print(rectangle(5))
print(rectangle(5, 20))


#Default + Keyword + Calculation
def bill(price, quantity=1, discount=0):
    total = price * quantity
    total = total - (total * discount / 100)
    return total

print(bill(100))
print(bill(100, 2))
print(bill(100, discount=10))
print(bill(100, 2, 10))

#Student Marks
# Q17. Create a function student(name, maths=0, python=0, dsa=0).
# Return the total marks.
# Test the function using different combinations.

def student(name, maths=0, python=0, dsa=0):
    total = maths + python + dsa
    return name, total

print(student("Ravi"))
print(student("Sita", 80, 90))
print(student("Rahul", python=85, dsa=90))

