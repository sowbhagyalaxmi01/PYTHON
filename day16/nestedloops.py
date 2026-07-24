#Print 2×2 stars
for i in range(2):
    for j in range(2):
        print("*",end="")
    print() 

#Print 3×4 stars
for i in range(3):
    for j in range(4):
        print("*",end="")
    print()   

#Print 5×5 square
for i in range(5):
    for j in range(5):
        print("1",end="")
    print()


#Print 4×6 ones
for i in range(1,5):
    for j in range(1,7):
        print("*",end="")
    print()
for i in range(4):
    for j in range(6):
        print("1",end="")
    print()

#Print row numbers
for i in range(3):
    for j in range(3):
        print(i,end="")
    print()    


#Print column numbers
for i in range(3):
    for j in range(3):
        print(j,end="")
    print()  

for i in range(1,4):
    for j in range(1,4):
        print(j,end="")
    print()      


#Print row & column numbers
for i in range(3):
    for j in range(3):
        print(i,j,end=" ")#print(f"{i},{j}",end="")
    print()  

for i in range(1,4):
    for j in range(1,4):
        print(i,j,end="")
    print()      

#Print coordinates
for i in range(3):
    for j in range(3):
        print(f"({i},{j})",end="")
    print()


#Print A in a grid
for i in range(3):
    for j in range(3):
        print("A",end="")
    print()    

#Print # in a grid  
for i in range(3):
    for j in range(3):
        print("#",end="")
    print()  

#Print 123 in every row
for i in range(1,4):
    for j in range(1,4):
        print(j,end="")
    print()  

#Print ABC in every row                                 
for i in range(3):
    for j in "ABC":
        print(j,end="")
    print() 


#Print multiplication table (1–5)
for i in range(1,6):
    for j in range(1,6):
        print(i,"*",j,"=",i*j)
    print()

#Print all (i,j) pairs
for i in range(1,3):
    for j in range(1,3):
        print(f"{i},{j}",end=" ")
    print()

#Print each row number once
for i in range(3):
    for j in range(1):
        print(i)

#Print each column number once
for i in range(1):
    for j in range(3):
        print(j)

#Print matrix row-wise
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in matrix:#for row in matrix:
    for j in i:#for value in row:
        print(j, end=" ")#print(value, end=" ")
    print()

# Print matrix column-wise                    
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for j in range(3):
    for i in range(3):
        print(matrix[i][j], end=" ")
    print()

#Print row sums  
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    total = 0
    for value in row:
        total += value
    print(total)

#Print column sums  
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for j in range(3):
    total = 0
    for i in range(3):
        total += matrix[i][j]
    print(total)
