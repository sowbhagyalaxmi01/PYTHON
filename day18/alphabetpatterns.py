#Fixed Alphabet Patterns

#Square of A
for i in range(3):
    for j in range(3):
        print("A",end="")
    print()    

#Rectangle of B
for i in range(3):
    for j in range(5):
        print("B",end="")
    print()    

#Row Alphabets
for i in range(4):
    for j in range(4):
        print(chr(65+i),end="")
    print()    


#Column Alphabets
for i in range(4):
    for j in range(4):
        print(chr(65+j),end="")
    print()    

#Alphabet Matrix
letters="ABC"
for i in range(3):
    for ch in letters:
        print(ch, end="")
    print()  


#Increasing Alphabet Patterns
#Alphabet Triangle

for i in range(4):
    for j in range(i+1):
        print(chr(65+j),end="")
    print() 

#Same Letter Triangle
for i in range(4):
    for j in range(i+1):
        print(chr(65+i), end="")
    print()

#Continuous Letters
ch = 65

for i in range(4):
    for j in range(i+1):
        print(chr(ch), end="")
        ch += 1
    print()

#Right-Aligned Alphabet Triangle
n = 4
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(i+1):
        print(chr(65+j), end="")
    print()    

#Alphabet Pyramid
n = 4

for i in range(n):

    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print increasing letters
    for j in range(i + 1):
        print(chr(65 + j), end="")

    # Print decreasing letters
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end="")

    print()    


#Decreasing Alphabet Patterns
#Reverse Triangle
for i in range(4):
    for j in range(4-i):
        print(chr(65+j), end="")
    print()


 #Reverse Same Letters
for i in range(4):
    for j in range(4-i):
        print(chr(65+i), end="")
    print()

#Reverse Right-Aligned Alphabet Triangle
n = 4

for i in range(n):

    # Spaces increase
    for j in range(i):
        print(" ", end="")

    # Letters decrease
    for j in range(n-i):
        print(chr(65+j), end="")

    print()

#Reverse Alphabet Pyramid
n = 4

for i in range(n):

    # Spaces
    for j in range(i):
        print(" ", end="")

    # Increasing letters
    for j in range(n-i):
        print(chr(65+j), end="")

    # Decreasing letters
    for j in range(n-i-2, -1, -1):
        print(chr(65+j), end="")

    print()   

#Reverse Continuous Letters
n = 4
ch = 65

for i in range(n):
    for j in range(n-i):
        print(chr(ch), end="")
        ch += 1
    print()

#Mixed alphabet patterns
#Alphabet Diamond
n = 4

# Top
for i in range(n):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print(chr(65+j), end="")

    for j in range(i-1, -1, -1):
        print(chr(65+j), end="")

    print()

# Bottom
for i in range(n-2, -1, -1):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print(chr(65+j), end="")

    for j in range(i-1, -1, -1):
        print(chr(65+j), end="")

    print()

#Alphabet Half Diamond
n = 4

# Top
for i in range(n):
    for j in range(i+1):
        print(chr(65+j), end="")
    print()

# Bottom
for i in range(n-2, -1, -1):
    for j in range(i+1):
        print(chr(65+j), end="")
    print()

#Alphabet Butterfly
n = 4

for i in range(n):

    # Left letters
    for j in range(i+1):
        print(chr(65+j), end="")

    # Middle spaces
    for j in range(2*(n-i-1)):
        print(" ", end="")

    # Right letters
    for j in range(i+1):
        print(chr(65+j), end="")

    print()

#Alphabet Hourglass
n = 4

# Top
for i in range(n):

    for j in range(i):
        print(" ", end="")

    for j in range(n-i):
        print(chr(65+j), end="")

    for j in range(n-i-2, -1, -1):
        print(chr(65+j), end="")

    print()

# Bottom
for i in range(1, n):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print(chr(65+j), end="")

    for j in range(i-1, -1, -1):
        print(chr(65+j), end="")

    print()            

#Alphabet Christmas Tree
# Small Pyramid
n = 3

for i in range(n):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print(chr(65+j), end="")

    for j in range(i-1, -1, -1):
        print(chr(65+j), end="")

    print()

# Large Pyramid
n = 4

for i in range(n):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print(chr(65+j), end="")

    for j in range(i-1, -1, -1):
        print(chr(65+j), end="")

    print()

# Trunk
for i in range(2):
    print("   |")   