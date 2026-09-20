#Factorial
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))


#Sum of numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

#Reverse a string
def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]

print(reverse("hello"))


#Fibonacci
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

print(fib(5))


#Count digits 
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print(count_digits(12345))


#Print numbers from 1 to N
def numbers(n):
    if n==0:
        return 
    numbers (n-1)
    print(n)
print(numbers(5))


#Print numbers from N to 1
def numbers(n):
    if n==0:
        return 
    print(n)
    numbers(n-1)
numbers(5)   


#Find the sum of numbers from 1 to N using recursion.
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)

print(sum(5))    


# Sum of digits
def sum(n):
    if n==0:
        return 0
    return n%10+sum(n//10)
print(sum(1234))

#Find the largest digit
def largest(n):
    if n == 0:
        return 0

    return max(n % 10, largest(n // 10))
print(largest(123445))


#Find the smallest digit
def smallest(n):
    if n <10:
        return n
    return min(n % 10, smallest(n // 10))
print(smallest(12345))