#Add two numbers
def add(a,b):
    return a+b
print(add(20,30))

#Check even or odd
def check_even_odd(n):
    if n %2==0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(23))    

def check_even_odd(a):
  if a %2==0:
      return "Even"
  else:
      return "Even"
m=int(input())
print(check_even_odd(m))
  
#for 2 numbers check
def check_even_odd(a, b):
    if a % 2 == 0:
        result1 = "Even"
    else:
        result1 = "Odd"
    if b % 2 == 0:
        result2 = "Even"
    else:
        result2 = "Odd"
    return result1, result2
m, n = map(int, input().split())
print(check_even_odd(m,n))



#Find square
def square(n):
    return n*n
print(square(n))

def square(n):
    return n*n
a=int(input())
print(square(a))


#Find maximum of two numbers
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
print(maximum(2,3))    



#Calculate simple interest
def simple_interest(p,r,t):
    return p*t*r/100
print(simple_interest(2,3,4))

def simple_interest(p,r,t):
    return p*t*r/100
m,n,o=map(int,input().split())
print(simple_interest(m,n,o))


#Find factorial
def factorial(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
print(factorial(5))    


#Count digits
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count
print(count_digits(12345))


#Reverse a number
def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev
print(reverse_number(1234))


#Check palindrome number
def is_palindrome(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return original == rev
print(is_palindrome(121))

#. Sum of digits
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(digit_sum(1234))
