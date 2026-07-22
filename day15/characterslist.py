#Print each character of on new line.
s = "Python Programming"
for ch in s:
    print(ch)

#Print each character in one line separated by commas.
s="python"
for ch in s:
    print(ch,end=",")
print()    
print(",".join(s))#used to remove comma last

s = "python"
for ch in s:
    if ch != s[-1]:
        print(ch, end=",")
    else:
        print(ch)


#Print each character with its position.
s = "Python Programming"
position=1
for ch in s:
    print(position,ch)
    position+=1
#Print every character twice.  
s="python"
for ch in s:
    print(ch*2)


#Print only the vowels of
s="sowbhagya"
for ch in s:
    if ch.islower() and ch in "aeiou":
        print(ch)




 #Print every element
nums = [5, 10, 15, 20, 25]
for num in nums:
    print(num)


#Print each number on one line
numbers = [2, 4, 6, 8, 10]
for num in numbers:
    print(num, end=" ")

#print only the even numbers.
nums = [12, 45, 7, 89, 23, 18, 20]
for num in nums:
    if num % 2 == 0:
        print(num)

#Print each number along with its square.      
nums = [12, 45, 7, 89, 23]
for num in nums:
    print(num, num**2)


#Find the sum of all numbers.
nums = [12, 45, 7, 89, 23]
total = 0
for num in nums:
    total += num

print(total)