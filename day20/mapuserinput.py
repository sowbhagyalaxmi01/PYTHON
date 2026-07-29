#map is used take more than one variable
def fun_add(a,b):
    return a+b
m,n=map(int,input().split(","))
print(fun_add(m,n))



#Without unpacking operations returns in tuple form
def operations(a,b):
    return a+b ,a-b,a*b,a/b
m,n=map(int,input().split())
print(operations(m,n))

#packing operations
def operations(a, b):
    return a + b, a - b, a * b, a / b
a, b = map(int, input().split())
addition, subtraction, multiplication, division = operations(a,b)

print(addition)
print(subtraction)
print(multiplication)
print(division)