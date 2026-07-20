#Find length without len()
s="sowbhagya"
count=0
for ch in s:
    count+=1
print(count)


#Reverse a string.
s="sowbhagya"
print(s[::-1])


#Check palindrome.
d="madam"
if d==d[::-1]:
    print("palindrome")
else:
    print("not palindrome")   


#Count vowels. 
s="sowbhagya"
count=0
for ch in s.lower():
    if ch in "aeiou":
        count+=1
print(count)

#Count consonants.
s="sowbhagya12%"
count=0
for ch in s.lower():
    if ch.isalpha() and ch not in"aeiou":
        count+=1
print(count)

#Count uppercase letters.
s="Sowbhagya"
count=0
for ch in s:
    if ch.isupper():
        count+=1
print(count)

#print ch lowercase letters.
s="Sowbhagya"
for ch in s:
    if ch.islower():
      print(ch)

# Count digits.     
d="sow2334%"
count=0
for ch in d:
    if ch.isdigit():
        count+=1
print(count)


#Count special characters.
d="sow2334%"
count=0
for ch in d:
    if not ch.isalnum():
        count+=1
print(count)

#Remove spaces.
s="sowbhagya laxmi"
print(s.replace(" ",""))

#Replace spaces with -
s="sowbhagya laxmi"
print(s.replace(" ","-"))

#Remove vowels.
s="sowbhagya"
result=""
for ch in s.lower():
    if ch  not in "aeiou":
        result+=ch
print(result)

#Remove duplicate characters.
s="madam"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)        

#Print duplicate characters.
s="madam"
result=""
for ch in s:
    if ch in result:
        result+=ch    
print(result)

#Find first non-repeating character.
s="sowbhagya"
for ch in s:
    if s.count(ch)==1:
       print(ch)
       break



#Find first repeating character.
s="sowbhagya"
for ch in s:
    if s.count(ch)>1:
        print(ch)
        break

#Frequency of each character.
s="testing tap"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)        


#Check anagram.
s1="silent"
s2="listen"
if sorted(s1)==sorted(s2):
    print("anagram")
else:
    print("not anagram")


#Check rotation.
s1="abcd"
s2="cdab"
if len(s1)==len(s2) and s2 in (s1+s1):
    print("rotation")
else:
    print("not rotation")


#Find longest word.
s="python is programming language"
words=s.split()
longest=words[0]
for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)











#Reverse each word.
s="this is a laptop"
words=s.split()
for word in words:
    print(word[::-1], end=" ")

#Reverse word order.
s = "I am learning Python"
words = s.split()
rev = words[::-1]
print(" ".join(rev))


#Capitalize first letter of every word.
s="apple"
print(s.title())

#Convert lowercase to uppercase without .upper().
s="sowbhagya"
result="" 
for ch in s:
    result+=chr(ord(ch)-32)
print(result)    
    

#Convert uppercase to lowercase without .lower().
s="sowbhagya"
result="" 
for ch in s:
    result+=chr(ord(ch)+32)
print(result)    


#Toggle case.
s = "SoWbHaGyA"
result = ""
for ch in s:
    if ch.islower():
        result += chr(ord(ch) - 32)
    else:
        result += chr(ord(ch) + 32)

print(result)


#Count occurrences of a character.
s="sowbhagya"
target="a"
count=0
for ch in s:
   if ch==target:
       count+=1
print(count)       

#Check substring.
s="sowbhagya"
if "bha" in s:
    print("True")
else:
    print("False")  


#Print ASCII values.
ch="d"
print(ord(ch))


#Print only alphabets.
s="sowhh34%@"
result=""
for ch in s:
    if ch.isalpha():
        result+=ch
print(result)       


#Print only digits.
s="sowhh34%@"
result=""
for ch in s:
    if ch.isdigit():
        result+=ch
print(result)     


#Remove digits.
s="sowhh34%@"
result=""
for ch in s:
    if not ch.isdigit():
        result+=ch
print(result)  

    











