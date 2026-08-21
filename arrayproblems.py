#1. Find the largest element in an array
arr = [10, 25, 7, 40, 15]

largest = arr[0]

for i in arr:
    if i > largest:
        largest = i

print("Largest:", largest)

#Find the smallest element
arr = [10, 25, 7, 40, 15]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest:", smallest)