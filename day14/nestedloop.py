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