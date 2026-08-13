# Create a decorator that prints "Welcome!" before calling the original function.
def welcome(func):
    def wrapper():
        print("Welcome!")
        func()
    return wrapper

@welcome
def hello():
    print("Hello")

hello()


# Create a decorator that takes the result of a function and doubles it.
def double(func):
    def wrapper():
        result = func()
        return result * 2
    return wrapper

@double
def number():
    return 5

print(number())

# Create a decorator that squares the result of a function.
def square(func):
    # your code
    pass

@square
def number():
    return 4

print(number())

#Add two numbers
def decorator(func):
    def wrapper(a, b):
        print("Calculating...")
        return func(a, b)
    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(3, 5))

# Create a decorator that prints the function name before calling it.
def show_name(func):
    def wrapper():
        print("Function:", func.__name__)
        func()
    return wrapper


@show_name
def hello():
    print("Hello")


hello()

#Create a decorator that checks whether the number is positive before calling the function.
def positive(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        else:
            print("Number is not positive")
    return wrapper


@positive
def square(n):
    return n * n


print(square(5))
print(square(-2))

#Create a decorator that converts the function's returned string to uppercase.
def upper(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper


@upper
def message():
    return "hello python"


print(message())

#Create a decorator that multiplies the result of a function by 10.
def multiply(func):
    def wrapper(a, b):
        result = func(a, b)
        return result * 10
    return wrapper


@multiply
def add(a, b):
    return a + b


print(add(2, 3))

#Create a decorator that allows a function to run only if age >= 18.
def check_age(func):
    def wrapper(age):
        if age >= 18:
            return func(age)
        else:
            print("Not allowed")
    return wrapper


@check_age
def enter(age):
    print("Welcome")


enter(20)
enter(15)