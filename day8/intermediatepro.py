#Divisible by 5
num=int(input("enter a number:"))
if num %5==0:
    print(num,"is divisible by 5")
else:
    print(num,"not divisible by 5")

#Divisible by 3 and 7
num=int(input("enter a number:"))
if num %3==0 and num %7==0:
    print(num,"divisible by both 3 and 7")
else:
    print(num," not divisible by both 3 and 7")

#Largest of Two Numbers
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
if a>b:
    print(a,"is largest")
elif b>a:
    print(b,"is largest")
else:
    print("both are equal")

#Smallest of Three Numbers
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
c=int(input("enter a number3:"))
if a<=b and a<=c:
    print(a,"is smallest")
elif b<=a and b<=c:
    print(b,"is smallest")
else:
    print(c,"is smallest")

#Number of Digits
num=int(input("enter a number:"))
if len(str(num))==1:#by converting num to str we find len (because num is int doesnot have count menthod)#if num<=9
    print("has one digit")
elif len(str(num))==2:
    print("has two digits")
elif len(str(num))==3:
    print("has three digits")
else:
    print("more than three digits")
    #    or
#     if 0 <= num <= 9:
#     print("One digit")
# elif 10 <= num <= 99:
#     print("Two digits")
# elif 100 <= num <= 999:
#     print("Three digits")

#Even Positive Number
num=int(input("enter a number:"))
if num>0 and num %2==0:
    print(num,"Positive Even Number")
else:
    print(num,"Not a Positive Even Number")

#Admission Eligibility
Marks=float(input("enter a marks:" ))
Age=int(input("enter a age:" ))
if Marks >=75 and Age >=18:
    print("Eligible")
else:
    print("not eligible")

#Triangle Type
a=int(input("enter a side1:"))
b=int(input("enter a side2:"))
c=int(input("enter a side3:"))
if a==b==c:
    print("equilateral traingle")
elif a==b or a==c or b==c:
    print("Isosceles triangle")
else:
    print("scalene triangle")

#Character Type
ch=input("enter a character:")
if ch.isupper():
    print(ch,"is uppercase")
elif ch.islower():
    print(ch,"is lowercase")
elif ch.isdigit():
    print(ch,"is digit")
else:
    print("special character")

#Weekday
day=int(input("enter a number:"))
if day==1:
    print("Monday")
elif day==2:
    print("tuesday")
elif day==3:
    print("wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("sunday")
else:
    print("Invalid Day")

#Electricity Bill
unit=int(input("enter a unit:"))
if unit<=100:
    bill=unit*2
elif unit<=200:
    bill=unit*3
else:
    bill=unit*5
print("Finalbill=",bill)


#employee Bonus
salary=int(input("enter salary:"))
if salary >=50000:
    bonus=salary*0.20
elif salary >=30000:
    bonus=salary*0.10
else:
    bonus=salary*0.50
final_salary=salary+bonus
print("final salary=",final_salary)    


#ATM Withdrawal
balance=int(input("enter balance:"))
withdrawl_amount=int(input("enter withdrawl amount:"))
if balance>=withdrawl_amount:
    print("Transaction Successful")
else:
    print("Insufficient Balance")

#Leap Year (Without copying)
year=int(input("enter a year:"))
if (year % 400==0) or (year % 4==0 and year % 100!=0):
    print(year,"Leap Year")
else:
    print(year,"Not a Leap Year")

#Age Category
age=int(input("enter a age:"))
if age >=0 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior citizen")

#Temperature
temp=float(input("enter a temperature:"))
if temp<=15:
    print("cold")
elif temp<=30:
    print("warm")
else:
    print("hot")

#Movie Ticket
age=int(input ("enter age:"))
if age<5:
    print("free ticket")
elif age>=5 and age<=17:
    print("₹100 charge")
elif age>=18 and age<=59:
    print("₹200 is charge")
else:
    print("₹150 is charge")

#FizzBuzz
num=int(input("enter a number:"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("print the number",num)

#Check whether a character is vowel ,consonant,digit,specila character:
ch=input("enter a character:")
if ch.lower() in "aeiou":
    print("vowel")
elif ch.isalpha() and ch.lower() not in "aeiou":
    print("consonant")
elif ch.isdigit():
    print("digit")
else:
    print("special character")

#Check whether three sides can form a valid triangle
a=int(input("enter a side1:"))
b=int(input("enter a side2:"))
c=int(input("enter a side3:"))
if a+b>c and a+c>b and c+b>a:
    print("valid traingle")
else:
    print("Invalid Triangle")

#Take three angles.
a=int(input("enter a angle1:"))
b=int(input("enter a angle2:"))
c=int(input("enter a angle3:"))
if a+b+c==180:
    print("valid traingle")
else:
    print("Invalid Triangle")

#Take three numbers.
#Print the middle number (neither largest nor smallest).
num1=int(input("enter a num1:"))
num2=int(input("enter a num2:"))
num3=int(input("enter a num3:"))
if (a>b and a<c) or (a <b and a>c):
   print(a, "is the middle number")
elif (b > a and b < c) or (b < a and b > c):
    print(b, "is the middle number")
else:
    print(c, "is the middle number") 
    

#Create a simple calculator.
first_num=int(input("enter a first number:"))
operator=input("enter a operator:")
second_num=int(input("enter a second number:"))
if operator == "+":
    print(first_num + second_num)
elif operator == "-":
    print(first_num - second_num)
elif operator == "*":
    print(first_num * second_num)
elif operator == "/":
    print(first_num / second_num)
else:
    print("Invalid Operator")








     






