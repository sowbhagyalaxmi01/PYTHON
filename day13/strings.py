#Remove Special Characters
s="abc@1234,"
result=""
for ch in s:
    if ch.isalnum():
        result+=ch
print(result)       


#Sort characters
s="sowbhagya"
result="".join(sorted(s))#convert into list and join 
print(result)

#Lexicographically Largest Character
#Find the largest character according to dictionary order
s="partner"
largest=s[0]
for ch in s:
    if ch>largest:
        largest=ch
print(largest)

#Lexicographically Smallest Character
o="sitha"
smallest=s[0]
for ch in o:
    if ch<smallest:
        smallest=ch
print(smallest)


#Check Pangram=A pangram contains all 26 English letters.
#Check whether a sentence contains every alphabet at least once.
a="i am practicing python"
letters = set()
for ch in s.lower():
    if ch.isalpha():
        letters.add(ch)

if len(letters) == 26:
    print("Pangram")
else:
    print("Not Pangram")


 #. Print Words One Per Line
s = "Python is easy"
words = s.split()
for word in words:
    print(word)


    

    