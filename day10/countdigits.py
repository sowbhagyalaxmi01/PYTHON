#Count the number of digits in a number.
s=input("enter a number:")
print(len(s))

s=int(input("enter a number:"))
count=0
while s>0:
    count+=1
    s//=10
print(count)

#Find the sum of digits.
s=input("enter a number:")
sum=0
for num in s:
    sum+=int(num)
print(sum)

num=1234
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num//=10
print(sum)


#Reverse a number
n=input("enter a number:")
rev=""
for num in n:
    rev=num+rev
print(rev)

n = 1234
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10
print(rev)

num = int(input("Enter a number: "))

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num //= 10

print(largest)


#Find the smallest digit in a number.
num = int(input("Enter a number: "))
smallest = 0
while num > 0:
    digit = num % 10

    if digit < smallest:
        smallest = digit

    num //= 10

print(smallest)

#Check whether a number is a palindrome.

n = input("Enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


n = 121
temp = n
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#Print each digit of a number
num = int(input("Enter a number: "))

while num > 0:
    digit = num % 10
    print(digit)
    num //= 10


#Count even digits
num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count += 1

    num //= 10

print(count)

#Count odd digits
num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        count += 1

    num //= 10

print(count)

#product of digits
num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

print(product)


#Average of digits
num = int(input("Enter a number: "))

total = 0
count = 0

while num > 0:
    digit = num % 10
    total += digit
    count += 1
    num //= 10

print(total / count)

#. Last digit
num = int(input("Enter a number: "))

print(num % 10)

#First digit
num = int(input("Enter a number: "))
while num >= 10:
    num //= 10
print(num)

#Count zeros
num = int(input("Enter a number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit == 0:
        count += 1

    num //= 10

print(count)

#Count occurrences of a digit
num = int(input("Enter a number: "))
search = int(input("Enter digit to search: "))

count = 0

while num > 0:
    digit = num % 10

    if digit == search:
        count += 1

    num //= 10

print(count)