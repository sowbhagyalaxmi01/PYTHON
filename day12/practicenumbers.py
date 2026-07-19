#Print different data types and type .
a=10.01
print(type(a))
b=10
print(type(b))
c="12"
print(type(c))
d=bool("")
print(type(d))
print(bool(" "))
print(bool(1))
e=10j
print(type(e))

#Convert int to float.
a=float(10)
print(a)
print(type(a))

#Convert float to int.
a=int(12.345)
print(a)
print(type(a))

#Convert int to string.
d=str(123)
print(d)
print(type(d))

#Convert string to int.
v=int("123")
print(v)
print(type(v))

#Swap two numbers.
a=12
b=34
a,b=b,a
print("a=",a)
print("b=",b)

#Find memory address using id().
a=10
print(id(a))


#Check identity using is
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a==b)

#Take two numbers and perform all arithmetic operations.
a=45
b=67
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Power =", a ** 2)

#Calculate simple interest.
a=12000
c=2
s=2
print("simple interest=",a*c*s/100)

#Calculate area of a circle.
radius=12
area=3.14*(radius**2)
print(area)

#Calculate area of a rectangle.
length=23
breadth=45
print("area of rectangle=",length*breadth)

#Calculate average of 5 numbers.
a=2
b=4
c=5
d=6
f=3
print("average=",a+b+c+d+f/2)

#Calculate BMI.
weight=60
height=1.65
bmi = weight / (height ** 2)
print("BMI =", bmi)
