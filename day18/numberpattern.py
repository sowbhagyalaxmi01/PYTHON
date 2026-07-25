#Fixed Number Patterns
#Square of 1s
# Fixed rows and columns
for i in range(4):
    for j in range(4):
        print(1, end="")
    print()

#Rectangle of 5s
# Rectangle
for i in range(3):
    for j in range(5):
        print(5, end="")
    print()

#Square of Row Numbers
# Row number changes
for i in range(1,5):
    for j in range(4):
        print(i, end="")
    print()

#Square of Column Numbers
# Column number changes
for i in range(4):
    for j in range(1,5):
        print(j, end="")
    print()

#Number Matrix
for i in range(3):
    for j in range(1,4):
        print(j, end="")
    print()


#Increasing Number Patterns  
#Increasing Triangle
for i in range(4):
    for j in range(i+1):
        print(j+1,end="")
    print()   

#Same Number Triangle    
for i in range(4):
    for j in range(i+1):# for j in range(i):
        print(i+1,end="")#  print(i,end="")
    print()  

#Continuous Numbers
num = 1

for i in range(4):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()

#Right-Aligned Number Triangle
n = 4

for i in range(n):

    # Spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Numbers
    for j in range(i+1):
        print(j+1, end="")

    print()

#Number Pyramid
n = 4

for i in range(n):

    # Spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Increasing numbers
    for j in range(i+1):
        print(j+1, end="")

    # Decreasing numbers
    for j in range(i-1,-1,-1):
        print(j+1, end="")

    print()

 #Decreasing Number Patterns
 #Reverse Triangle
n = 4

for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()

#Reverse Same Number Triangle
n = 4

for i in range(1,n+1):
    for j in range(n-i+1):
        print(i,end="")
    print()

#Reverse Right-Aligned Triangle
n = 4

for i in range(n):

    # Spaces increase
    for j in range(i):
        print(" ", end="")

    # Numbers decrease
    for j in range(n-i):
        print(j+1, end="")

    print()

#Reverse Pyramid
n = 4

for i in range(n):

    # Spaces
    for j in range(i):
        print(" ", end="")

    # Increasing
    for j in range(n-i):
        print(j+1, end="")

    # Decreasing
    for j in range(n-i-2,-1,-1):
        print(j+1, end="")

    print()

#Reverse Continuous Numbers
n = 4
num = 1

for i in range(n):

    for j in range(n-i):
        print(num, end=" ")
        num += 1

    print()

#Mixed Number Patterns
#Number Diamond
n = 4

# Top
for i in range(n):

    # Spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Increasing
    for j in range(i+1):
        print(j+1, end="")

    # Decreasing
    for j in range(i-1,-1,-1):
        print(j+1, end="")

    print()

# Bottom
for i in range(n-2,-1,-1):

    # Spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Increasing
    for j in range(i+1):
        print(j+1, end="")

    # Decreasing
    for j in range(i-1,-1,-1):
        print(j+1, end="")

    print()


#Number Half Diamond
n = 4

# Top
for i in range(n):
    for j in range(i+1):
        print(j+1, end="")
    print()

# Bottom
for i in range(n-2,-1,-1):
    for j in range(i+1):
        print(j+1, end="")
    print()

#Number Butterfly
n = 4

for i in range(n):

    # Left
    for j in range(i+1):
        print(j+1, end="")

    # Spaces
    for j in range(2*(n-i-1)):
        print(" ", end="")

    # Right
    for j in range(i+1):
        print(j+1, end="")

    print()

#Number Hourglass
n = 4

# Top
for i in range(n):

    for j in range(i):
        print(" ", end="")

    for j in range(n-i):
        print(j+1, end="")

    for j in range(n-i-2,-1,-1):
        print(j+1, end="")

    print()

# Bottom
for i in range(1,n):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1):
        print(j+1, end="")

    for j in range(i-1,-1,-1):
        print(j+1, end="")

    print()

#Floyd's Triangle
num = 1
n = 5

for i in range(n):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()

#Pascal's Triangle
n = 4

for i in range(n):

    num = 1

    for j in range(n-i-1):
        print(" ", end=" ")

    for j in range(i+1):
        print(num, end="   ")
        num = num*(i-j)//(j+1)

    print()

#Palindrome Number Pyramid
n = 4

for i in range(n):

    for j in range(n-i-1):
        print(" ", end="")

    for j in range(i+1,0,-1):
        print(j,end="")

    for j in range(2,i+2):
        print(j,end="")

    print()

#Reverse Palindrome Pyramid
n = 4

for i in range(n):

    for j in range(i):
        print(" ", end="")

    for j in range(n-i,0,-1):
        print(j,end="")

    for j in range(2,n-i+1):
        print(j,end="")

    print()


#Zig-Zag Number Pattern
num = 1
n = 5

for i in range(n):

    temp = []

    for j in range(i+1):
        temp.append(num)
        num += 1

    if i % 2 == 1:
        temp.reverse()

    for x in temp:
        print(x, end=" ")

    print()


#Spiral Number Pattern
n = 4

matrix = [[0]*n for _ in range(n)]

top = 0
bottom = n-1
left = 0
right = n-1
num = 1

while top <= bottom and left <= right:

    for i in range(left, right+1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom+1):
        matrix[i][right] = num
        num += 1
    right -= 1

    for i in range(right, left-1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top-1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(*row)
                        