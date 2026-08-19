#. Generate numbers from 1 to 5
def numbers():
    for i in range(1, 6):
        yield i          # Gives one value at a time(yield is like return, but it doesn't end the function.)

for num in numbers():
    print(num)


#Generate even numbers
def squares(n):
    for i in range(1, n + 1):
        yield i * i      # Generate square

for num in squares(5):
    print(num)


#Generate numbers using next()
def numbers():
    yield 10
    yield 20
    yield 30

g = numbers()

print(next(g))    # Gets 10
print(next(g))    # Gets 20
print(next(g))    # Gets 30


#Generate odd numbers
def odd_numbers(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            yield i      # Generate odd number

for num in odd_numbers(10):
    print(num)


#Generator for Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        yield a          # Give current Fibonacci number
        a, b = b, a + b  # Move to next numbers

for num in fibonacci(7):
    print(num)

        
