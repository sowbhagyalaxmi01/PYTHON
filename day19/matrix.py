#Print Matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

#Row-wise Traversal
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

#Column-wise Traversal
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()

#Sum of All Elements
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)


#Maximum Element
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

largest = matrix[0][0]

for row in matrix:
    for value in row:
        if value > largest:
            largest = value

print(largest)


#Minimum Element
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

smallest = matrix[0][0]

for row in matrix:
    for value in row:
        if value < smallest:
            smallest = value

print(smallest)


#Search an Element
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

target = 5

for i in range(len(matrix)):
    for j in range(len(matrix[0])):

        if matrix[i][j] == target:
            print(i, j)


#Count Even Numbers
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

count = 0

for row in matrix:
    for value in row:
        if value % 2 == 0:
            count += 1

print(count)


#Count Odd Numbers
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

count = 0

for row in matrix:
    for value in row:
        if value % 2 != 0:
            count += 1

print(count)


#Print Boundary Elements
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

n = len(matrix)

for i in range(n):
    for j in range(n):

        if i==0 or j==0 or i==n-1 or j==n-1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")

    print()


