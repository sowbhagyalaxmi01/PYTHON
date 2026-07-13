#conditional statements:are used to make decisions in a program.They execute different blocks of code depending on whether condition is True or False.

#types of conditional statements:
#1.if statement:executes a block of code if condtion is True.
age=int(input("enter a age:"))
if age>=18:
    print("Eligible to vote")

#2.if-else Statement:else runs only if all previous conditions are False.
# Executes one block if the condition is true and another if it is false.
age = 10
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#3.elif statement:is used for checking multiple conditions.if the first if condition is False.
#  we can have multiple elif condtions in a code.
#With elif Python stops checking once it finds the first True condition.
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")

#without elif if we use if condition it checks all conditions are checked independently.
marks = 85
if marks >= 90:
    print("A")
if marks >= 80:
    print("B")
if marks >= 70:
    print("C")


#4.Nested if Statement:
#An if statement inside another if statement.
#It is used when you want to check a second condition only if the first condition is True.
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Eligible to vote")

