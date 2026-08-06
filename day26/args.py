#*args used to collect extra positional arguments into  tuple form.
def my_funtion(*kids):
    print(kids)
my_funtion(10,20,30,40)


#Arbitary arguments
def my_funtion(*kids):
    print("the youngest child",kids[2])or  print("The youngest child is " + kids[2])

my_funtion("emil","tobias","linus")   

#Accessing individual arguments from *args:
def arguments(*args):
    print("type:",type(args))
    print("first argument:",args[0])
    print("second argument:",args[1])
    print("All arguments:",args)
arguments("emil","scoot","deew")    


#Using *args with Regular Arguments
def my_funtion(greeting,*names):#python matches arg with parameters:greeting "hello",names ("emil","dear","lit","jee")
    for name in names:           #Because greeting is a normal parameter, so it takes the first argument.*names collects all remaining arguments into a tuple.
        print(greeting,name)
my_funtion("hello","emil","dear","lit","jee")        


#A function that calculates the sum of any number of values:
def sum_values(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
print(sum_values(1,2,3))
print(sum_values(10,20,30))
print(sum_values(5))


#Finding the maximum value:
def maximum(*numbers):
    max=numbers[0]
    for num in numbers:
        if num>max:
            max=num
    return max
print(maximum(2,3,4,7))  #but this method fails will give u index error.because when numbers=() and no numbers[0]

#method 2      
def my_function(*numbers):
    if len(numbers) == 0:
        return None

    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

print(my_function(3, 7, 2, 9, 1))


#calculate average
def average(*args):
    total=0
    for x in args:
        total+=x
    return total/len(args)
print(average(10,20,30))


def average(*args):
    count=0
    total=0
    for x in args:
        count+=1
        total+=x
    return total/count
print(average(10,20,30))


#Separate even and odd
def separate(*args):
    even=[]
    odd=[]
    for x in args:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
print(separate(1, 2, 3, 4, 5, 6))


#Find minimum and maximum
def min_max(*args):
    minimum=args[0]
    maximum=args[0]
    for x in args:
        if x<minimum:
            minimum=x
        if x>maximum:
            maximum=x    
    return minimum,maximum
print(min_max(10, 5, 30, 2, 15))


#Count positive and negative numbers
def count_numbers(*args):
    positive = 0
    negative = 0

    for x in args:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1

    return positive, negative

print(count_numbers(10, -5, 8, -2, 0, 7))


#Find numbers greater than a given value
def greater_than(n, *args):
    result = []

    for x in args:
        if x > n:
            result.append(x)

    return result

print(greater_than(10, 5, 15, 20, 7, 30))


#Multiply all numbers
def multiply(*args):
    result = 1

    for x in args:
        result *= x

    return result

print(multiply(2, 3, 4))