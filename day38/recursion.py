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