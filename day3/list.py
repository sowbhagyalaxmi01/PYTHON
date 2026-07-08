#Create a list of 5 numbers and print it.
list=[1,2,3,4,5]
for x in list:
    print(x)

#Print the first element of a list.
list=[1,2,3,4,4]
print(list[0])

#Print the last element of a list.
list=[1,2,3,4,5]
print(list[-1])

#Find the length of a list without using len().
list=[1,2,3,4,4]
count=0
for x in list:
    count+=1
print(count)    

#Print all elements using a while loop.
list=["a","d","g"]
i=0
while i<len(list):
    print(list[i])
    i+=1

#Find the sum of all elements.
list=[1,2,5,7,8]
sum=0
for num in list:
    sum+=num
print(sum)

#Find the largest element.
list=[1,4,7,9,12]
largest=list[0]
for num in list:
    if num>largest:
        largest=num
print(largest)

#Find the smallest element.
list=[45,7,-3,6,-9]
smallest=list[0]
for num in list:
    if num<smallest:
        smallest=num
print(smallest)

#Count the number of even and odd numbers.
list=[2,4,5,86,54,-2]
even=0
odd=0
for num in list:
    if num%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)



