#printa all postional args and sum the *arg
def show(a,b,*c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print(sum(c)) #sum works on tuple or for print(list(sum(c)))   
show(12,67,45,89)   


#Write a function that accepts any number of numbers and returns their sum.
def total(*args):
    return sum(args)
print(total(10,23,45))


#Sum first two separately and remaining values
def show(a, b, *c):
    first = a + b
    remaining = sum(c)

    return first, remaining

print(show(10, 20, 30, 40, 50))


#Sum only odd numbers
def odd_sum(*args):
    total = 0

    for x in args:
        if x % 2 != 0:
            total += x

    return total

print(odd_sum(10, 15, 20, 25, 30))

#Sum values greater than 10
def greater_sum(*args):
    total = 0

    for x in args:
        if x > 10:
            total += x

    return total

print(greater_sum(5, 10, 15, 20, 25))


#Take input from the user
values = list(map(int, input("Enter values: ").split()))

print(sum(values))


#program to fun a+b and sum all values
def calculate(a,b,*args):
   print(a+b)
   print(a+b+sum(*args))
values=list(map(int,input().split()))
calculate(values)