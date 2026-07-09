#Check if an element exists.
t = (10, 20, 30, 40)
print(20 in t)

#Count occurrences of an element.
t = (1, 2, 2, 3, 2)
print(t.count(2))

#Find the index of an element.
t = (10, 20, 30, 40)
print(t.index(30))

#Concatenate two tuples.
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)

#Repeat a tuple.
t = (1, 2)
print(t * 3)

#Convert a list to a tuple.
lst = [1, 2, 3]
t = tuple(lst)
print(t)

#Convert a tuple to a list.
t = (4, 5, 6)
lst = list(t)
print(lst)

#Find the maximum element
t = (10, 40, 20, 50, 30)
print(max(t))

#Find the sum of all elements
t = (10, 20, 30, 40)
print(sum(t))

#Find the average of tuple elements
t = (10, 20, 30, 40)
print(sum(t) / len(t))

#Sort a tuple
t = (30, 10, 40, 20)
print(tuple(sorted(t)))

#Find the second largest element
t = (10, 40, 20, 50, 30)
x = sorted(t)
print(x[-2])

#Find the second smallest element
t = (10, 40, 20, 50, 30)
x = sorted(t)
print(x[1])

#Merge two tuples and remove duplicates
t1 = (1, 2, 3)
t2 = (3, 4, 5)
print(tuple(set(t1 + t2)))

#Swap two tuples
t1 = (1, 2)
t2 = (3, 4)
t1, t2 = t2, t1
print(t1)
print(t2)

#Find common elements in two tuples
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
print(tuple(set(t1) & set(t2)))

#Find the frequency of every element
t = (1, 2, 2, 3, 1, 2)
for i in set(t):
    print(i, t.count(i))

#Find the product of all elements
t = (2, 3, 4)
product = 1
for i in t:
    product *= i
print(product)    

#Rotate a tuple left by one position
t = (1, 2, 3, 4)
print(t[1:] + t[:1])

#Rotate a tuple right by one position
t = (1, 2, 3, 4)
print(t[-1:] + t[:-1])



