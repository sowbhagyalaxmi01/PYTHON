#Count the frequency of a given character using loops.
s="sowbhagya"
target="a"
count=0
for ch in s:
    if ch==target:
        count+=1
print(count)        
#using str.count()
s="sowbhagya"
target="a"
print(s.count(target))

#using indexes
s="hidden"
target = "a"
count = 0
for i in range(len(s)):
    if s[i] == target:
        count += 1
print(count)

#using dictionary
s = "sowbhagya"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq["a"])

#Count the frequency of every character.
s="sowbhagya"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)            


#Remove all spaces from a string.

s="never give up"
print(s.replace(" ",""))
#using loop
s = "never give up"
result = ""
for ch in s:
    if ch != " ":
        result += ch
print(result)

#Replace spaces with hyphens.
s="never give up"
print(s.replace(" ","-"))

#Remove all vowels.
s="code of python"
result=""
for ch in s.lower():
    if ch not in "aeiou":
        result+=ch
print(result)       


#Remove duplicate characters.
s="saturday"
result=""
for ch in s:
    if ch not in result:
        result+=ch
print(result)    


#Find the first non-repeating character.
s = "sowbhagya"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break


#Find the first repeating character.
s="samples"
for ch in s:
    if s.count(ch)>1:
        print(ch)
        break

#Check whether two strings are anagrams.
s1="listen"
s2="slient"
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("not Anagrams")    


#Check whether one string is a substring of another.
s1="south india"
s2="uth"
if s2 in s1:
    print("yes")
else:
    print("no")    


#Find all occurrences of a character.
s="varitey"
for i, ch in enumerate(s):
    if ch == "t":
     print(i)
 #range
s="banana"
target = "a"
for i in range(len(s)):
    if s[i] == target:
       print(i)    

 #list in
s = "banana"
target = "a"

result = []

for i, ch in enumerate(s):
    if ch == target:
        result.append(i)

print(result)      