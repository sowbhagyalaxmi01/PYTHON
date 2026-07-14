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