#Half Diamond
n=4
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()    
for i in range(n-2,-1,-1):
    for j in range(i+1):
        print("*",end="")
    print()        


#Full Diamond
n=4
#top
for i in range(n):
    for j in range(n-i-1):
        print (" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()

#bottom       
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print (" ",end="")
    for j in range(2*i+1):
        print("*",end="")
    print()     

#butterfly
n = 4

# -------- Top --------
for i in range(n):

    # Left stars
    for j in range(i+1):
        print("*", end="")

    # Middle spaces
    for j in range(2*(n-i-1)):
        print(" ", end="")

    # Right stars
    for j in range(i+1):
        print("*", end="")

    print()

# -------- Bottom --------
for i in range(n-2,-1,-1):

    # Left stars
    for j in range(i+1):
        print("*", end="")
    # Middle spaces
    for j in range(2*(n-i-1)):
        print(" ", end="")
    # Right stars
    for j in range(i+1):
        print("*", end="")

    print() 

#Hour glasses
n = 4

# -------- Top --------
for i in range(n):

    # Print spaces
    for j in range(i):
        print(" ", end="")

    # Print stars
    for j in range(2*(n-i)-1):
        print("*", end="")

    print()


# -------- Bottom --------
for i in range(1, n):

    # Print spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Print stars
    for j in range(2*i+1):
        print("*", end="")

    print()       

# Christmas Tree

# -------- Small Pyramid --------
n = 3

for i in range(n):

    # Spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Stars
    for j in range(2*i+1):
        print("*", end="")

    print()


# -------- Large Pyramid --------
n = 4

for i in range(n):

    # Spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Stars
    for j in range(2*i+1):
        print("*", end="")

    print()


# -------- Tree Trunk --------
for i in range(2):      # 2 rows

    for j in range(3):  # Spaces before trunk
        print(" ", end="")

    print("|")  


#Sandglass Pattern
n = 4

# Top
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(n-i)-1):
        print("*", end="")
    print()

# Bottom
for i in range(1, n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()


#Double Pyramid
n = 3

for i in range(n):

    # Left spaces
    for j in range(n-i-1):
        print(" ", end="")

    # Left pyramid
    for j in range(2*i+1):
        print("*", end="")

    # Middle spaces
    for j in range(2*(n-i)-1):
        print(" ", end="")

    # Right pyramid
    for j in range(2*i+1):
        print("*", end="")

    print()

#Reverse Double Pyramid
n = 4

for i in range(n):

    # Left spaces
    for j in range(i):
        print(" ", end="")

    # Left stars
    for j in range(2*(n-i)-1):
        print("*", end="")

    # Middle spaces
    for j in range(2*i+1):
        print(" ", end="")

    # Right stars
    for j in range(2*(n-i)-1):
        print("*", end="")

    print()

 #X Pattern
n = 5

for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Plus (+) Pattern
n = 5
mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid or j == mid:
            print("*", end="")
        else:
            print(" ", end="")
    print() 