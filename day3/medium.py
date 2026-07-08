#Reverse a list without using reverse().
list=[1,2,3,4,5]
rev=[]
for num in list:
    rev=[num]+rev
print(rev)


#Check if an element exists in the list.
list=[2,56,7,88]
if 2 in list:
    print("yes")
else:
   print("no")    

#Count how many times an element appears.
list=[2,4,6,7,2,4,7,3,2]
count=0
for num in list:
   if num==2:
      count+=1
print(count)      

#Remove duplicate elements.
list=[2,4,6,7,2,4,7,3,2]
newlist=[]
for num in list:
   if num not in newlist:
      newlist.append(num)
print(newlist)

#Find the second smallest element.
list=[2,3,4,56,7]
smallest=list[0]
second=float('inf')
for num in list:
    if num<smallest:
      second=smallest
      smallest=num
    elif num<second and num!=smallest:
        second=num
print(second)        

#Find the second largest element.
list=[2,3,4,56,7]
largest=list[0]
second=float('-inf')
for num in list:
    if num>largest:
      second=largest
      largest=num
    elif num>second and num!=largest:
      second=num
print(second) 

#Merge two lists.
list1=[1,2,3]
list2=[4,6,7]
list1.extend(list2)#extend merge two list
print(list1)

#Copy a list without using copy().
list=[2,5,6]
mylist=list[:]#list(list)
print(mylist)

#Swap the first and last elements.
list=[2,3,4,5,6]
list[0],list[-1]=list[-1],list[0]
print(list)
   