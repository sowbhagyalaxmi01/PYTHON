#basic problem
def display():
    x = 10       # Local variable
    print(x)     # Python finds x in Local scope

display()


#Can we access a local variable outside
def test():
    x = 10

test()
print(x)#NameError:name 'x' is not defined


#Local variable created only when function runs
def test():
    x = 50
    print(x)

print("Before")
test()
print("After")#The local variable x is created when test() executes.


#Same variable name in different functions
def first():
    x = 10
    print(x)

def second():
    x = 20
    print(x)

first()
second()#Each function has its own local x.

#Local variable and if
def test():
    if True:
        x = 10

    print(x)

test()#Python does not create a separate scope for an if block. x is still local to test().


#Local variable before assignment
x = 100

def test():
    print(x)
    x = 20

test()
#UnboundLocalError:x=20 inside the function and therefore treats x as local throughout that function.so print(x)  tries to use the local x before it has a value.

#local and global
x = 100          # Global

def display():
    x = 50       # Local
    print(x)     # L → finds 50

display()

print(x)         # Global x → 100


#sum
x = 10

def test():
    x = 20
    y = 30
    print(x + y)#x and y are local variables
test()

#if conditional block
def test():
    a = 10

    if True:
        b = 20       # Still inside function's local scope

    print(b)       


#range
def test():
    for i in range(3):
        x = i

    print(x)

test()
