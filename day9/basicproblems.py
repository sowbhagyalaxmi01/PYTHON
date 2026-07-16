#Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

#Print all even numbers from 1 to 20.
for i in range(2,21,2):
    print(i) 

#Print all odd numbers from 1 to 20.
for i in range(1,21,2):
    print(i)   

#Print the multiplication table of a given number.
s=int(input("enter a number:"))    
for i in range(1,11):
    print(s,"x",i,"=", s*i)

# Print the first 20 natural numbers using a while loop.
i=1
while i<=20:
    print(i)
    i+=1

#Print numbers from 1 to 100 that are divisible by 5.
for i in range(1,101):
    if i%5==0:
        print(i)    

#Print numbers from 1 to 50 except multiples of 3.
for i in range(1,51):
    if i%3==0:
        continue
    print(i)

#Print numbers from 1 to 20 and stop when the number is 15.
for i in range(1,21):
    if i==15:
        break
    print(i)   

#Print all numbers from 1 to 20 in reverse order.
for i in range(20,0,-1):
    print(i)

          
   
