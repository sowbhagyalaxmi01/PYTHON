#Fixed rows and columns, then changing columns.

#Square#row=col
for i in range(3):
    for j in range(3):
        print("*",end="")
    print()

#Rectangle rows!=colu
for i in range(3):
    for j in range(5):
        print("*",end="")
    print()

#Wide Rectangle
for i in range(2):
    for j in range(7):
        print("*",end="")
    print()

#Tall Rectangle
for i in range(6):
    for j in range(2): 
        print("*",end="")
    print()     

#Hash (#) Square
for i in range(3):
    for j in range(3):
        print("#",end="")
    print()     

#. Dollar ($) Rectangle
for i in range(4):
    for j in range(4):
        print("$",end="")
    print()     


#INCREASING ORDER PATTERNS 
#LEFT ALIGNED INCREASING
#row fixed and colums(i+1)
#right angle traingle
for i in range(4):
    for j in range(i+1):
        print("*",end="")
    print()    

#Right Triangle (5 rows)
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

# Increasing by Steps
 #Increase by 2 stars  
for i in range(4):
    for j in range(2*(i+1)):
        print("*",end="")
    print()   

#Increase by 3 stars
for i in range(4):
    for j in range(3*(i+1)):
        print("*",end="")
    print()

#Wide Triangle
for i in range(5):
    for j in range(2*(i+1)):
        print("*",end="")
    print() 


#Triangle using $
for i in range(4):
    for j in range(i+1):
        print("$",end="")
    print()  

#Right-Aligned Increasing
# Right Triangle  
#Spaces = n-i-1(spaces decrease)
#Stars = i+1(stars increase)
n=4   
for i in range(n): 
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()   

#Right Triangle (5 rows)      
n=5
for i in range(n): 
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()  

#Right Triangle using #
n=4   
for i in range(n): 
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("#",end="")
    print()   


#Centered Increasing
# Full Pyramid 
#Spaces = n-i-1
#Stars = 2*i+1
n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()     

#Wide Pyramid
#Logic: Even number of stars.Spaces decrease.Stars increase by 2 each row.
n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(2*(i+1)):
        print("*",end="")
    print()     


#Arrow Head
#No spaces.
#Stars increase in odd numbers.
#Formula: 2*i + 1
n=4
for i in range(n):
    for j in range(2*i+1):
        print("*",end="")
    print()  


#DECREASING PATTERNS
#Left-Aligned Inverted Triangle
#range(n-i)
#n=4 or drt for i in range(4):
for i in range(4):
    for j in range(n-i):
        print("*",end="")
    print()   

#Decrease by 2 Stars  
for i in range(4):
    for j in range(2*(n-i)):
        print("*",end="")
    print()  


#Right-Aligned Inverted Triangle
#Spaces = i
#Stars = n-i
n = 4

for i in range(n):

    # Spaces increase
    for j in range(i):
        print(" ", end="")

    # Stars decrease
    for j in range(n-i):
        print("*", end="")

    print()

#centered
#Inverted Pyramid
##Spaces = i
#Stars = 2*(n-i)-1
#Even stars = 2*(n-i)
n = 4

for i in range(n):

    # Spaces increase
    for j in range(i):
        print(" ", end="")

    # Odd stars decrease
    for j in range(2*(n-i)-1):
        print("*", end="")

    print()     


#Reverse Wide Pyramid 
n = 4

for i in range(n):

    # Spaces increase
    for j in range(i):
        print(" ", end="")

    # Even stars decrease
    for j in range(2*(n-i)):
        print("*", end="")

    print()   