#sum of 2 numbers
def sum(a,b):
    return a+b
add=sum(3,5)
print(add)

#even or odd
def check_evenodd(n):
    if n%2==0:
        return True
    else:
        return False
print(check_evenodd(4))    


#return a funtion square
def square(n):
    print( n*n)
print(square(4))

#create fun to find largest of 2 numbers
def largest(a,b):
    if a>b:
        return a
    else:
        return b
print(largest(23,45))

#factorial
def fact(n):
   i=1
   fact=1
   while i<=n:#for i in range(1,n+1):
       fact*=i
       i+=1
   return fact
print(fact(7))  

#count digits
def count(n):
    count=0
    while n>0:
        n//=10
        count+=1
    return count
print(count(12345))    

#Reverse a number
def reverse(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev   
print(reverse(2345))


#sum of digits
def sum(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n//=10
    return total
print(sum(1111111234))

#Check palindrome number
def palindrome(n):
    original=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n//=10
    if original==rev:
       return True
    else:
       return False  
print(palindrome(1234))     

# string method
def palindrome(n):
    n = str(n)
    return n == n[::-1]
print(palindrome(1221))

def palindrome(n):
    if n==n[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome("swetha"))    


#Armstrong Number
def is_armstrong(n):
    original = n
    total = 0
    digits = 0
    temp = n

    while temp > 0:
        digits += 1
        temp //= 10

    temp = n

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return original == total

print(is_armstrong(153)) 
    
