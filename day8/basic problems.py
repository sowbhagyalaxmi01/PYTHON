#Print "Positive" if it is greater than 0.
num=int(input("enter a number:"))
#check if num is greater than 0 
if num >0:
    print("Postive")

#Check Even Number (Only if)
# Take an integer input
num = int(input("Enter a number: "))

# Check if the number is divisible by 2
if num % 2 == 0:
    # Print if the condition is true
    print("Even")

#Voting Eligibility
# Take age as input
age = int(input("Enter your age: "))

# Check whether age is 18 or above
if age >= 18:
    # Print eligible message
    print("Eligible to vote")

#Even or Odd
# Take an integer input
num = int(input("Enter a number: "))

# Check if the number is even
if num % 2 == 0:
    # Print Even
    print("Even")
else:
    # Otherwise print Odd
    print("Odd")


#Greatest of Two Numbers
# Take first number
a = int(input("Enter first number: "))

# Take second number
b = int(input("Enter second number: "))

# Compare both numbers
if a > b:
    # Print first number
    print(a, "is greater")
else:
    # Print second number
    print(b, "is greater")


#Password Check
# Take password from the user
password = input("Enter password: ")

# Check if password is correct
if password == "python123":
    # Login successful
    print("Login Successful")
else:
    # Wrong password
    print("Wrong Password")

#Grade Calculator
# Take marks as input
marks = int(input("Enter marks: "))

# Check highest grade first
if marks >= 90:
    print("Grade A")

# Check second grade
elif marks >= 80:
    print("Grade B")

# Check third grade
elif marks >= 70:
    print("Grade C")

# Default grade
else:
    print("Grade D")


#Positive, Negative or Zero
# Take integer input
num = int(input("Enter a number: "))

# Check positive
if num > 0:
    print("Positive")

# Check negative
elif num < 0:
    print("Negative")

# Otherwise number is zero
else:
    print("Zero")

#Season Based on Month
# Take month number
month = int(input("Enter month (1-12): "))

# Winter months
if month == 12 or month == 1 or month == 2:
    print("Winter")

# Summer months
elif month == 3 or month == 4 or month == 5:
    print("Summer")

# Rainy months
elif month == 6 or month == 7 or month == 8:
    print("Rainy")

# Autumn months
elif month == 9 or month == 10 or month == 11:
    print("Autumn")

# Invalid month
else:
    print("Invalid Month")

#Nested if (Age and ID)
# Take age
age = int(input("Enter age: "))

# Take ID status
has_id = input("Do you have ID (yes/no): ")

# Check age first
if age >= 18:

    # Check ID only if age condition is true
    if has_id == "yes":
        print("Entry Allowed")
    else:
        print("Bring ID")

# Age is below 18
else:
    print("Not Eligible")                

#Login System
username=input("enter username:")
password=input("enter password:")
if username=="admin":
    if password=="admin123":
        print("Login Successful")
    else:
        print("Incorrect Password")    
else:
    print("Invalid Username")       


#Largest of Three Numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a >=b and a>=c:
    print(a,"is greatest number ")
elif b>=c and b>=a:
    print(b,"is greatest number")
else:
    print(c," is greast number")

#Leap Year
year=int(input("enter a year:"))
if (year % 400==0) or (year % 4==0 and year % 100!=0):
    print(year,"Leap Year")
else:
    print(year,"Not a Leap Year")

#Vowel or Consonant
ch=input("enter a charcter:")
if ch in "aeiouAEIOU":#len(ch)==1
    print("Vowel")
else:
    print("Consonant")

#Discount Calculator
amount=float(input("enter purchase amount:"))
if amount >=6000:
    discount=amount*0.20
elif amount>=2500:
    discount=amount*0.10
else:
    discount=0
final_amount=amount-discount
print("Discount=",discount)
print("Final Amount=",final_amount)


