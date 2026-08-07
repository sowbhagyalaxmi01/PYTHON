#scope is a region in a program where a variable can be accesed(used).
x=10
print(x)#x can be used it is un scope.


#Python has 4 types of scope, known as LEGB:
#L → Local → Enclosing → Global → Built-in

#Local Scope
#A variable created inside a function. It can be accessed only inside that function.
def my_function():
    x = 10
    print(x)

my_function()


#Global Scope
# A variable created outside all functions has global scope.
x = 30
def my_function():
    print(x)

my_function()


#Enclosing Scope
# A variable in an outer function is in the enclosing scope of an inner function.
def outer():
    x = 20

    def inner():
        print(x)

    inner()

outer()


#Built-in Scope
#Built-in scope contains names that Python provides automatically.
# ex:print(),len(),sum(),max(),min()
numbers = [10, 20, 30]
print(len(numbers))


#One Complete Example
x = "Global"   # Global scope
def outer():
    y = "Enclosing"    # Enclosing scope for inner()

    def inner():
        z = "Local"    # Local scope of inner()

        print(z)             # L → finds z here → "Local"
        print(y)             # L ❌ → E ✅ → finds y in outer()
        print(x)             # L ❌ → E ❌ → G ✅ → finds x globally
        print(len("Python")) # L ❌ → E ❌ → G ❌ → B ✅ → len() 
    inner()                    # Calls inner()
outer()                         # Calls outer()
