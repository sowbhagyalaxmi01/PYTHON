# Call the function using unpacking
def student(name,age):
    print(name)
    print(age)
data={
    "name":"ram",
    "age":20
}
student(**data)


#find sum
def sum(a,b,c):
    return a+b+c
numbers={
    "a":23,
    "b":45,
    "c":34
}
print(sum(**numbers))


#Predict the output.by key names, not by the dictionary's orderr.
def show(name, city):
    print(name, city)

data = {
    "city": "Hyderabad",
    "name": "Anu"
}

show(**data)


#employee
def employee(id, salary):
    print(id)
    print(salary)

emp = {
    "id": 101,
    "salary": 50000
}
emp(**emp)

#type error of missing 1 reqd postional arg'age'
def student(name, age):
    print(name, age)

data = {
    "name": "Ravi"
}

student(**data)


#type error:add() got an unexpected keyword arg 'c'
def add(a, b):
    print(a+b)

data = {
    "a": 5,
    "b": 8,
    "c": 10
}

add(**data)


#contain of default value executes code.
def add(a, b):
    print(a+b)

data = {
    "a": 5,
    "b": 8,
    "c": 10
}

add(**data)