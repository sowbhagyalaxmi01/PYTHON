#sets{} are used to store multiple items in single variable and is collection of unordered,doesnot allow duplicates.

#create a set with numbers 1, 2, 3, 4, 5.
s={1,2,3,4,5}
print(s)

#Add an element 6 to a set.
s={1,2,3,4,5}
s.add(6)
print(s)

#Remove an element 3 from a set.
s={1,2,3,4,5,6}
s.remove(3)#s.discard(10)   # No error
print(s)

#Check if 10 exists in a set.
s={1,2,3,4,5}
print(10 in s)   
#loop
if 10 in s:
    print("True")
else:
    print("False") 


#Find the length of a set.
s={1,2,3,4,5}
print(len(s))

#Iterate through all elements in a set.
s={1,2,3,4,5}
for value in s:
   print(value)

#Clear all elements from a set.
s={1,2,3,4,5}
print(s.clear())
print(s)
print(type(s))

#Copy a set.
s={1,2,3,4,5}
d=s.copy()
print(d)

#Find the maximum element in a set.
d={1,2,3,4,5}
print(max(d))

#Find the minimum element in a set.
d={1,2,3,4,5}
print(min(d))


#Remove duplicate elements from a list using a set.
d=[1,1,3,2,3,4,5]
print(set(d))


#Count the number of unique elements in a list.
l=[1,2,3,4,5,6,4,2,1]
count=0
unique=[]
for num in l:
    if num not in unique:
        count+=1
print(count) 

#Find common elements between two sets.
d={1,2,4,5}
x={2,3,6,7}
print(d&x)

#Find elements present in the first set but not in the second.
d={1,2,4,5}
x={2,3,6,7}
print(d-x)

#Find elements present in either set but not both.
d={1,2,4,5}
x={2,3,6,7}
print(d^x)


#Check if one set is a subset of another.
d={1,3}
x={1,2,3,6,7}
print(d.issubset(x))

#check if two sets are disjoint.
d={1,2,4,5}
x={2,3,6,7}
print(d.isdisjoint(x))

#Merge two sets.
d={1,2,4,5}
x={2,3,6,7}
d.update(x)
print(d)

#Remove all duplicate words from a sentence.
s="I am pursing graduation graduation"
print(set(s.split()))

#Convert a string into a set of unique characters.
s="sowbhagya"
print(set(s))    







    