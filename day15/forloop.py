#Print numbers from 1 to 10.
for i in range(1,11):
    print(i)


#Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

#  Print all even numbers from 1 to 20.
for i in range(2,21,2):
    print(i) 

#Print all odd numbers from 1 to 20.
for i in range(1,21,2):
    print(i)


#Print the multiples of 5 from 1 to 50.
n=5
for i in range(1,51,5):
    print(i)
for i in range(1,51):
    if i %5==0:
        print(i)    
   

#Print the square of numbers from 1 to 10.
for i in range(1,11):
    print(i**2)  


#Print the cube of numbers from 1 to 10.
for i in range(1,11):
    print(i**3)  

#Print the first 10 natural numbers in one line separated by spaces.
for i in range(1,11):
    print(i,end=" ")
print()
  
          

#Print the multiplication table of 7.  
n=7
for i in range(1,11):
    print(n,"x",i, "=",n*i) 


#Print all numbers from 50 to 100 that are divisible by 5.
for i in range(50,101):
    if i%5==0:
       print(i)


#Print all lowercase letters from a to z.
for i in range(ord('a'),ord('z')+1):
    print(chr(i))


#Print each character on a new line.
s="python"
for ch in s:
    print(ch)

#Print each color on a new line.
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)


#Print numbers from 1 to 20, but print only those divisible by 3.
for i in range(1,21):
    if i%3==0:
        print(i)


#Print numbers from 1 to 30.
# If the number is:
# divisible by 3, print "Fizz"
# divisible by 5, print "Buzz"
# divisible by both 3 and 5, print "FizzBuzz"
# otherwise, print the number
for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
