#enclosing scope
def outer():
    x=10
    def inner():
        print(x)
    inner()
outer()     


#problem 2
def outer():
    x=10
    def inner():
        nonlocal x
        x=20
        print(x)
    inner()
outer()        


#problem 3
## # Since count belongs to the outer function, increment() needs nonlocal count to modify it.
# Create an outer function `counter()`
def counter():
# Create a variable `count = 0` inside counter()    
    count=0
# Create an inner function `increment()`    
    def increment():
    # Increase count by 1 inside increment()
        nonlocal count
        count+=1
    # Call increment() three times    
    increment()    
    increment()    
    increment() 
 # Print count inside counter()    
    print(count)
counter()



# problem 4
def calculator():
    result = 10

    def add():
        nonlocal result
        result += 5

    def multiply():
        nonlocal result
        result *= 2

    add()
    multiply()

    print(result)

calculator()