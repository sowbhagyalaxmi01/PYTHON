#Find all vowels in a string using a set.
s="sowbhagya"
vowels=set()
for ch in s.lower():
    if ch in "aeiou":
        vowels.update(ch)#use vowels.add(ch)
print(vowels)     

#Check whether two strings contain the same unique characters.
s1="poojitha"
s2="sai kiran"
if set(s1)==set(s2):
    print("True")
else:
    print("False")   

#Find the first repeated character in a string using a set.
s="sowbhagya"
seen=set()#empty set
for ch in s:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)
        
   
#Count how many distinct characters are present in a string.
s="shiva shankar"
print(len(set(s.replace(" ",""))))#dont want spacing

#Find the missing numbers from 1 to n using sets.
nums={1,2,3,4,6}
n=6
all_nums = set(range(1, n+1))#range(1,2,3,4,5,6) by set {1,2,3,4,5,6}
print(all_nums - nums)

#Remove duplicate characters while keeping only unique ones
s="sowbhagyalaxmi" 
print(set(s))   #set keyword removes duplicates


#Find the union of two sets.
s={1,2,3,4,5}
d={3,5,5,6}
print(s|d)#combine all elements

#Find the intersection of two sets.
s={1,2,3,4,5}
d={3,5,5,6}
print(s&d)#common elements
