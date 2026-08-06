#Take one collection (list/tuple) and separate it into individual values.


def add(a, b, c):
    print(a)
    print(b)
    print(c)

numbers = [10, 20, 30]

add(*numbers)

#step 1:numbers=[1,2,3]
#step 2:python sees add(*numbers) it automatically changes it to add(10,20,30)
#Now parameter matching happens a=10,b=20,c=30
#output:10
        # 20
        # 30


#without unpacking  
def add(a, b, c):
    print(a + b + c)
numbers = [10, 20, 30]#it thinks like add([10,20,30]) it assigns as a=[10,20,30]
add(numbers)          #b=? c=?
#output:type error missing postional arg


#multiply
def multiply(a, b):
    return a*b

nums=[5,6]

print(multiply(*nums))


# Tuple unpacking
def display(x,y,z):
    print(x,y,z)

t=(1,2,3)

display(*t)


#Less values than parameters
def add(a,b,c):
    print(a+b+c)
nums=[10,20]
add(*nums)
#outpt:type error :misssing 1 postional arg'c'



#*args
def add(*nums):
    print(nums)

numbers=[10,20,30]

add(*numbers)#(10,20,30)


#
def student(name, age, city):
    print(name)
    print(age)
    print(city)

details=["Ravi",20,"Hyderabad"]

student(*details)
#output:Ravi 
        #20
        #Hyderabad


# conclusion:*args in the function definition = Collect many values into one tuple.
# * before a list/tuple in the function call = Unpack one list/tuple into many values.        