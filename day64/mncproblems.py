# 1. Print Hello World without using a variable.
print("Hello World")
# 2. Swap two numbers without a third variable.
a=23
b=34
a,b=b,a
print(a,b)
# 3. Check whether a number is positive, negative or zero.
n=int(input("enter a number:"))
if n>0:
    print("positive")
elif n<0:
    print("negative")
else:
    print("Zero")        
# 4. Find the largest of three numbers.
def largest(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
print(largest(10,20,30))    
# 5. Check whether a number is even or odd.
def check_number(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(check_number(27))    
# 6. Calculate factorial.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))        
# 7. Generate Fibonacci numbers.
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
print(fibonacci(7))        
# 8. Check whether a number is prime.
def prime(n):
   count=0
   for i in range(1,n+1):
       if n%i==0:
           count+=1
   if count==2:
       return "prime"
   else:
       return "not prime"
print(prime(7))          
               

# 9. Reverse an integer.
def rev(n):
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev
print(rev(134))        
# 10. Find the sum of digits of a number.
def sum(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n//=10
    return total
print(sum(123))    
# 11. Reverse a string.
def rev_str(s):
    return s[::-1]
print(rev_str("skill"))
# 12. Check whether a string is a palindrome.
def palindrome(s):
    if s==s[::-1]:
        return "palindrome"
    else:
        return "not palindrome"
print(palindrome("madam"))    
# 13. Count vowels and consonants.
def count_vowel_cons(s):
    vowels=0
    consonants=0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return vowels,consonants
print(count_vowel_cons("I am a student"))                    
# 14. Count the frequency of every character.
def freq_char(s):
    freq={}
    for ch in s:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq
print(freq_char("height"))           
# 15. Find the first non-repeating character.
def non_repeating_char(s):
    for ch in s:
        if s.count(ch)==1:
            print(ch)
            break
non_repeating_char("swiss")    

# 16. Remove duplicate characters from a string.
def duplicates(s):
    result=""
    for ch in s:
        if ch not in result:
            result+=ch
    return result
print(duplicates("programming"))        
# 17. Check whether two strings are anagrams.
def anagrams(s1,s2):
    if sorted(s1)==sorted(s2):
        print("anagrams")
    else:
        print("not anagrams")
anagrams("silent","listen")            
# 18. Find the longest word in a sentence.
def longest_word(sentence):
    words=sentence.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
print(longest_word("i am learning python"))        
# 19. Count words in a sentence.
def count_words(sentence):
    words=sentence.split()
    return len(words)
print(count_words("i stay in hyderabad"))

# 20. def compress(chars):
def compress(chars):
    result = []
    i = 0
    while i < len(chars):
        count = 1
        while i + 1 < len(chars) and chars[i] == chars[i + 1]:
            count += 1
            i += 1
        result.append(chars[i])
        if count > 1:
            result.append(str(count))
        i += 1
    return result
chars = ["a", "a", "b", "b", "c", "c", "c"]
print(compress(chars))

# 21. Find maximum and minimum in a list without max()/min().
def max_min(nums):
    maximum=nums[0]
    minimum=nums[0]
    for num in nums:
        if num>maximum:
            maximum=num
        if num<minimum:
            minimum=num
    return maximum,minimum
print(max_min([12,34,56,78]))     

# 22. Remove duplicates from a list.
def dup_lst(lst):
    result=[]
    for num in lst:
        if num not in result:
            result.append(num)
    return result
print(dup_lst([12,34,12,67,34]))        
# 23. Find the second-largest number.
def sec_largest(nums):
    unique=list(set(nums))
    unique.sort()
    return unique[-2]
print(sec_largest([1,2,5,2,4]))    
# 24. Reverse a list without reverse().
def rev(nums):
    result=[]
    for i in range(len(nums)-1,-1,-1):
        result.append(nums[i])
    return result
print(rev([12,34,56,44,45]))
    
# 25. Find common elements between two lists.
def common(a,b):
    common=[]
    for num in a:
        if num in b:
            common.append(num)
    return common
print(common([1,2,3],[2,4,1,5]))        
# 26. Merge two sorted lists.
def merge(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result
a = [1, 3, 5]
b = [2, 4, 6]
print(merge(a, b))
# 27. Move all zeros to the end.
def move_zeroes(a):
    result=[]
    for x in a:
        if x!=0:
            result.append(x)
    for x in a:
        if x==0:
            result.append(x)
    return result
print(move_zeroes([0,1,2,0,4,5,7,0,9]))                

# 28. Find missing numbers from a sequence.
def missing(a):
    for i in range(1,n+1):
        if i not in a:
          return i
print(missing([1,2,3,5,6]))        
# 29. Rotate a list by k positions.
def rotate(a, k):
    k = k % len(a)
    return a[-k:] + a[:-k]
a = [1, 2, 3, 4, 5]
k = 2
print(rotate(a, k))

# 30. Find duplicate elements.
def duplicates(a):
    result=[]
    for x in a:
        if a.count(x)>1 and x not in result:
            result.append(x)
    return result
print(duplicates([1,2,3,2,4,1]))    


#31.Count word frequency using a dictionary
def word_freq(s):
    d={}
    for word in s.split():
        if word in d:
            d[word]+=1
        else:
            d[word]=1
    return d
print(word_freq("apple is good for health apple good"))  


#32.Find the most frequent element.
def most_freq(a):
    count={}
    for x in a:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    return max(count,key=count.get)
print(most_freq([1,2,3,4,2,3,2,6,4]))       


#33.Group words that are anagrams.
def group_anagrams(words):
    result = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in result:
            result[key] = []
        result[key].append(word)
    return list(result.values())
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))


#34.Invert a dictionary.
def inverted(d):
    result={}
    for key in d:
        result[d[key]]=key
    return result
print(inverted({"a":1,"b":2,"c":3}))   


#35. Merge two dictionaries.
def merge(d1,d2):
    result=d1.copy()
    for key in d2:
        result[key]=d2[key]
    return result
print(merge({"a":1,"b":2},{"c":3,"d":4}))


# 36. Find common keys between dictionaries.
def common_keys(a, b):
    return set(a.keys()) & set(b.keys())


a = {"name": "Ram", "age": 20, "city": "Hyd"}
b = {"age": 21, "city": "Delhi", "course": "CSE"}

print(common_keys(a, b))
# 37. Find unique elements using sets.
def unique_elements(a):
    return set(a)


a = [1, 2, 2, 3, 4, 4, 5]

print(unique_elements(a))
# 38. Build a student grade tracker.
def grade_tracker(students):
    for name, marks in students.items():
        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        else:
            grade = "D"

        print(name, grade)


students = {
    "Ram": 95,
    "Sita": 82,
    "John": 65,
    "Sam": 45
}

grade_tracker(students)
# 39. Create a phone-book application.
def phone_book():
    contacts = {}

    contacts["Ram"] = "9876543210"
    contacts["Sita"] = "9876501234"

    name = input("Enter name: ")

    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found")


phone_book()
# 40. Create a dictionary-based inventory system.
def inventory():
    items = {
        "apple": 10,
        "banana": 20,
        "mango": 15
    }

    item = input("Enter item: ")

    if item in items:
        print("Quantity:", items[item])
    else:
        print("Item not found")


inventory()



