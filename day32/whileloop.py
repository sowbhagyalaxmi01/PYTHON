#print 1 to 5 using while loop
i=1
while i<=10:
    print(i)
    i+=1

#print 5 to 1
i=5
while i>=1:
    print(i)
    i-=1    

#print "Hello" 5 times
i=1
while i<=5:
    print("Hello")
    i+=1

#even from 2 to 20
i = 1

while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

i=2
while i<=20:
    print(i)
    i+=2    


#print odd
i=1
while i<=20:
    print(i)
    i+=2

#multiplication table of 5
i=1
while i<=10:
    print(5,"x",i ,"=",5*i)
    i+=1
#by giving n value
n=5
i=1
while i<=20:
    print(n*i)
    i+=1  

#find sum of number 1 to 10
count=0
i=1
while i<=10:
    count+=i
    i+=1    
print(count)    

#sum of even number from 1 to 10
count=0
i=2
while i<=10:
    count+=i
    i+=2
print(count)    


#count numbers 1 to 100 divisible by 5
count=0
i=1
while i<=100:
    if i %5==0:
        count+=1
    i+=1
print(count)        

count=0
i=5
while i<=100:
    count+=1
    i+=5

print(count)


#take numbers from user print number from 1 to n
n=int(input("enter a number:"))
i=1
while i<=n:
    print(i)
    i+=1


#factorial of number
i=1
fact=1
while i<=5:
    fact*=i
    i+=1
print(fact)    
      

#count number of digits in number
n = 12345
count = 0

while n > 0:
    n //= 10
    count += 1

print(count)

#sum of digits
n=12345
total=0
while n>0:
    digit=n%10
    total+=digit
    n//=10
print(total)


#reverse number 
n=12346
reverse=""#rev=0
while n>0:
    digit=n%10
    reverse=reverse+str(digit)#reverse=reverse*10+digit
    n//=10
print(reverse)    


