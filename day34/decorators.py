#A decorator is used to add extra behavior to an existing function without changing its original code.
# @decorator is just a shorter way of applying the decorator to the function.
# The decorator function receives the original function.
# The wrapper function adds the extra behavior.
# @decorator connects them.
# When you call the original function name, you're actually calling the wrapper.



# This is the decorator function
# It receives the original function as an argument
def decorator(func):

    # This wrapper function adds extra behavior
    def wrapper():

        # Code that runs BEFORE the original function
        print("Before function")

        # Call the original function
        func()

        # Code that runs AFTER the original function
        print("After function")

    # Return the wrapper function
    return wrapper


# Apply the decorator to hello()
@decorator
def hello():

    # This is the original function code
    print("Hello")


# Call hello()
# Actually, because of @decorator, wrapper() is called
hello()