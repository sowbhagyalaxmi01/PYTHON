#Print * 3 times in 2 rows
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