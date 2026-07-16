#Find the sum of numbers from 1 to n.
n = int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#Find the sum of all even numbers from 1 to n.    
n = int(input("Enter a number: "))
sum=0
for i in range(2,n+1,2):
    if i%2==0:
        sum+=i
print(sum)    

#Find the sum of all odd numbers from 1 to n.
n = int(input("Enter a number: "))
sum=0
for i in range(1,n+1,2):
    if i%2!=0:
        sum+=i
print(sum)    

#Count how many even numbers are between 1 and 100.
even_count=0
for i in range(1,101):
    if i%2==0:
        even_count+=1
print(even_count)       


#Count how many odd numbers are between 1 and 100.
odd_count=0
for i in range(1,101):
    if i%2!=0:
        odd_count+=1
print(odd_count)    

#. Count how many numbers from 1 to 100 are divisible by both 3 and 5
count=0
for i in range(1,101):
    if i %3==0 and i%5==0:
       count+=1
print(count)


#Find the factorial of a number.
num=5
fact=1
for i in range(1,num+1):
    fact*=i
print(fact) 

#Find the product of numbers from 1 to n.
n = int(input("Enter a number: "))
product=1
for i in range(1,n+1):
    product*=i
print(product)

#find sum of numbers
n=5
sum=0
for i in range(1,n+1):
    sum+=i
    print(sum)

    