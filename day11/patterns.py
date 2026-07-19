#Print a Vertical Line of Stars
for i in range(5):
    print("*")

#Print a Horizontal Line of Stars
for i in range(5):
    print("*",end="")
   
#Print a Square Pattern 5*5
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()


#Print Repeated Row Numbers
for i in range(1,6):
    for j in range(5):
        print(i, end="")
    print()

#Print Repeated Column Numbers
for i in range(5):
    for j in range(1,6):
        print(j, end="")
    print()

#Print Consecutive Numbers
num = 1

for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

#Print Repeated Alphabets    
for i in range(3):
    for ch in "ABC":
        print(ch, end="")
    print()

#Print Alphabets Vertically
for ch in "ABCD":
    print(ch)

#Print Consecutive Alphabets
ch = ord('A')

for i in range(3):
    for j in range(3):
        print(chr(ch), end="")
        ch += 1
    print()

#Print a Right-Angled Triangle of Stars
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()

#Print an Inverted Triangle of Stars
for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()

#Print Increasing Numbers
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()    

