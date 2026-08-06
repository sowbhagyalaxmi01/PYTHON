#Kwargs Collect all remaining keyword arguments into a dictionary

def student(**kwargs):
    print(kwargs)

student(name="Sowbhagya", age=20, branch="CSm")
#output:{'name': 'Sowbhagya', 'age': 20, 'branch': 'CSE'}

#for dict form
def student(**kwargs):#intially in dict form converted
    for key, value in kwargs.items():#first :key = "name"  value = "Sowbhagya"
        print(key, value)#key = "age"
                         #value = 20

student(name="Sowbhagya", age=20)
#output:name Sowbhagya
        #:age 20



#Create a function that accepts any number of keyword arguments and prints them
def details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

details(name="Ravi", age=20, city="Hyderabad")


#Print only the values from kwargs.
def show_values(**kwargs):
    for value in kwargs.values():
        print(value)

show_values(name="Ravi", age=20, city="Hyderabad")


#Print only keys
def show_keys(**kwargs):
    for key in kwargs.keys():
        print(key)

show_keys(name="Ravi", age=20, city="Hyderabad")


#find number of keyword arguments
def count_details(**kwargs):
    return len(kwargs)

print(count_details(name="Ravi", age=20, city="Hyderabad"))

#Find the sum of all numeric values passed through kwargs.
def total(**kwargs):
    sum = 0

    for value in kwargs.values():
        sum += value

    return sum

print(total(a=10, b=20, c=30))


#Find maximum value
def maximum(**kwargs):
    max_value = None

    for value in kwargs.values():
        if max_value is None or value > max_value:
            max_value = value

    return max_value

print(maximum(a=10, b=50, c=20))


#Print students who scored above 50
def passed_students(**students):
    for name, marks in students.items():
        if marks > 50:
            print(name)

passed_students(
    Ravi=70,
    Sita=45,
    Arun=80,
    Priya=35
)


#Count values greater than 50
def count_passed(**students):
    count = 0

    for marks in students.values():
        if marks > 50:
            count += 1

    return count

print(count_passed(Ravi=70, Sita=45, Arun=80, Priya=35))


#Search for a particular key
def check_age(**kwargs):
    if "age" in kwargs:
        return "Age is present"
    else:
        return "Age is not present"

print(check_age(name="Ravi", age=20))


#Combine *args and **kwargs
def details(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword arguments:", kwargs)

details(10, 20, 30, name="Ravi", age=20)
#output:Arguments: (10, 20, 30)
       #Keyword arguments: {'name': 'Ravi', 'age': 20}