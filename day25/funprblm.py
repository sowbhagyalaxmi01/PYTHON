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
print(palindrome("sowbhagya"))    


#check prime
def check_prime(n):
    count=0

    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        return "Prime"
    else:
        return "Not prime"
print(check_prime(7))  

#code is correct for positive numbers greater than 1
def check_prime(n):#
    for i in range(2,n):
        if n%i==0:
            return "not prime"
    return "prime"
print(check_prime(7))    


#check prime number and include if call funtion as 1 and 0 also
def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        # If n is exactly divisible by i, it is not prime
        if n % i == 0:
            return False

    # No divisor was found, so n is prime
    return True

print(is_prime(11))



#. Find largest number in a list
def largest(n):
    max=n[0]
    for num in n:
        if num>max:
            max=num
    return max
print(largest([2,3,4,5]))   


#Count even numbers
def count_even(nums):
    count=0
    for num in nums:
        if num%2==0:
            count+=1
    return count
print(count_even([2,3,5,6,7]))        


#Check anagram
def anagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return "anagram"
    else:
        return "not anagram"
print(anagram("list","call"))
print(anagram("listen", "silent"))


#Find second largest
def second_largest(nums):
    first=second=float("-inf")
    for num in nums:
        if num > first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num
    return second
print(second_largest([10,20,30,40,50]))           


#Using sort()
def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]

print(second_largest([10, 20, 30, 40, 50]))



#index approach like nums[0].
def second_largest(nums):
    first=nums[0]
    second=nums[1]
    if second>first:
        first,second=second,first
    for i in range(2,len(nums)):
        if nums[i]>first:
            second=first
            first=nums[i]
        elif nums[i]>second:
            second=nums[i]
    return second
print(second_largest([10, 20, 30, 40, 50]))
              


#Remove duplicates
def remove_duplicates(nums):
    result=[]
    for num in nums:
        if num not in result:
            result.append(num)
    return result
print(remove_duplicates([2,34,5,2,7,8,4,8]))        


#Find frequency of each character
def frequency(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq 
print(frequency("hello"))


#Find common elements list
def common(a, b):
    result = []
    for n in a:
        if n in b and n not in result:
            result.append(n)
    return result
print(common([1, 2, 3, 4], [3, 4, 5, 6]))


#find repeated/common elements within only one list
def common_elements(nums):
    result = []
    for num in nums:
        if nums.count(num) > 1 and num not in result:
            result.append(num)
    return result
print(common_elements([1, 2, 3, 2, 4, 1]))


#Find the next prime
def next_prime(n):
    n += 1
    while True:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
                break
        if prime:
            return n
        n += 1
print(next_prime(10))