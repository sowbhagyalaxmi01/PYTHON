#Count vowels
def count_vowels(s):
    count=0
    for ch in s.lower():
        if ch in "aeiou":
            count+=1
    return count        
print(count_vowels("Saturday"))   

#Reverse a string
def reverse(s):
   return s[::-1]
s=input("enter a string:")
print(reverse(s))

def reverse(s):
    rev=""
    for ch in s:
        rev=ch+rev
    return rev
s=input("enter a string:")    
print(reverse(s))

#Check string palindrome
def palindrome(s):
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"


  
##. Sum of digits
def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
print(digit_sum(1234))




    