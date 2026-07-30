#Default argument means: a parameter already has a value, and Python uses that value if you don't provide one when calling the function.
#default is the value written inside the function definition.
def greet(name, message="Hello"):
    print(message, name)

greet("Ravi")
#name → no default
#message → default is "Hello"
#"Ravi" is the argument we gave to name.
#message was not given, so Python uses its default: