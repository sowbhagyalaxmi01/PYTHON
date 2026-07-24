#Write a Python program to print the following pattern:
# **
# **
for i in range(1):
    for j in range(1):
        print("*", end="")
    print()


#Write a Python program to print the following pattern:
# *
# *
# *

for i in range(3):
    print("*")

 #Write a Python program to print the following pattern:
# ***
# ***
# ***    
for i in range(3):
    for j in range(3):
        print("*", end="")
    print()

 #Write a Python program to print the following pattern:
# 111
# 111
# 111   

for i in range(3):
    for j in range(3):
        print(1, end="")
    print()


 #Write a Python program to print the following pattern:
# 123
# 123
# 123   
for i in range(3):
    for j in range(1, 4):
        print(j, end="")
    print()

##Print * 3 times in 2 rows
for i in range(2):
    for j in range(3):
        print("*",end="")
    print()

#Print number
for i in range(1, 3):
    for j in range(3):
        print(i, end="")
    print()

#Print AB
for i in range(3):
    for j in "AB":
        print(j, end="")
    print()

#Print 123
for i in range(2):
    for j in range(1, 4):
        print(j, end="")
    print()

#Print each row number once
for i in range(1, 4):
    for j in range(1):
        print(i)

#Print star
for i in range(4):
    for j in range(1):
        print("*")

#Print row and column numbers
for i in range(1,4):
    for j in range(1,4):
        print(i,j,end="")
    print()         


#Print coordinates
for i in range(1,4):
    for j in range(1,4):
        print(f"{i},{j}",end="")                            
    print()

#print letters
for i in "ABC":
    for j in range(3):
        print(i,end="")
    print() 
letters="ABC"
for i in letters:
    for j in range(3):
        print(i,end="")
    print()    


 #print rows and column values
for i in range(1,3):
    for j in range(1,3):
        print("i=",i,"j=",j)                  