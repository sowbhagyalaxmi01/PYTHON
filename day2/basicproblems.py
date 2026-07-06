# #length of str without len()
s="Luck"
count=0
for ch in s:
   count+=1
print(count)   

#reverse of string without slicing by each new character is added to the front.
s="python"
rev=""
for ch in s:
    rev=ch+rev
print(rev)

#string empty
s=""
if s=="":
    print("string is empty")
else:
    print("string is not empty")   

s="" 
if not s:
   print("string is empty")
else:
   print("string is not empty")
   


#vowels in string
s="Sowbhagya"
count=0
for ch in s.lower():
    if ch in "aeiou":
       count+=1
print(count)     

#consonants in string
s="Sowbhagya"
for ch in s.lower():
   if ch.isalpha() and ch not in "aeiou":
      print(ch)
  
#count upper ans lower case
s="Sowbhagya Laxmi"
lower=upper=0
for ch in s:
   if ch.islower():
      lower+=1
   elif ch.isupper():
     upper+=1
print("lower:",lower)  
print("upper:",upper)          


#Count digits, alphabets, and special characters.
s="sowbhagya@123"
digits=alphabets=special=0
for ch in s:
   if ch.isdigit():
      digits+=1
   elif ch.isalpha():
      alphabets+=1
else:
    special+=1
print("digits:",digits)
print("alphabets:",alphabets)
print("special character:",special)


#Check whether a string is a palindrome.
s="madam"
rev=""
for ch in s:
   rev=ch+rev
if rev==s:
    print("it is palindrome")
else:
    print("it is not palindrome")

#Find the first character of a string.
s="never give up"
print(s[0])

#Find the last character of a string.
s="i will do it"
print(s[-1])

#Print every character on a new line.
s="python"
for ch in s:
   print(ch)

#Find the ASCII value of every character.
s="python"
for ch in s:
   print(ch,ord(ch))

#Convert lowercase to uppercase without using upper().
s="sowbhagya"
result=""
for ch in s:
   result+=chr(ord(ch)-32)
print(result)   

#Convert uppercase to lowercase without using lower().
s="SOWBHAGYA"
result=""
for ch in s:
   result+=chr(ord(ch)+32)
print(result)   
   



   
