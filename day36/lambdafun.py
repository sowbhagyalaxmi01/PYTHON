#A lambda function is a small, one-line function.
#lambda arguments: expression
#lambda → tells Python "I'm creating a small function"
# a, b   → inputs
# :       → separates inputs from result
# a + b   → result


#Two numbers
multiply = lambda a, b: a * b

print(multiply(4, 5))


#Create a lambda function that returns the square of a numbe
square = lambda x: x * x

print(square(5))

#Create a lambda function that returns True if a number is even.
even = lambda x: x % 2 == 0

print(even(10))

#Create a lambda function that returns the bigger of two numbers.
big = lambda a, b: a if a > b else b

print(big(10, 20))

#Sort by second value
students = [("A", 80), ("B", 60), ("C", 90)]

result = sorted(students, key=lambda x: x[1])

print(result)


#