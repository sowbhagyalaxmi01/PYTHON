#Find the sum of all values in a dictionary.
d = {"a": 10, "b": 20, "c": 30}
total=0
for value in d.values():#print(sum(d.values()))
    total+=value
print(total)

#Find the maximum value.
d = {"a": 10, "b": 20, "c": 30}

values = list(d.values())
maximum = values[0]
for value in values:#print(max(d.values()))
    if value > maximum:
        maximum = value
print(maximum)

#Find the minimum value.
d = {"a": 10, "b": 20, "c": 30}
minimum=None
for value in d.values():
    if minimum is None or value<minimum:
        minimum=value
print(minimum)        


#Count how many values are even.
d = {"a": 10, "b": 20, "c": 30,"d":40}
even=0
odd=0
for value in d.values():
    if value%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)  
print("odd:",odd)         

#Multiply all values together.
d = {"a": 10, "b": 20, "c": 30,"d":40}
product=1
for value in d.values():
    product*=value
print(product)

   
#Create a new dictionary with all values doubled.
d = {"a":10, "b":20, "c":30, "d":40}

new = {}

for key, value in d.items():
    new[key] = value * 2

print(new)


#Swap keys and values.
d = {"a":10, "b":20, "c":30, "d":40}

new = {}

for key, value in d.items():
    new[value] = key

print(new)


#Merge two dictionaries.
d={"a":1,"b":2}
x={"e":4,"g":9}
d.update(x)
print(x)

#Clear all items from a dictionary.
d = {"a": 10, "b": 20, "c": 30,"d":40}
d.clear()
print(d)

#Count the frequency of each character in a string using a dictionary.
d="sowbhagya"
freq = {}
for ch in d:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print(freq)

#Count the frequency of each word in a sentence.
d = "this is a vscode page"
freq = {}
for word in d.split():
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)    

#Find the key with the highest value.
d = {"a":10,"b":20,"c":30,"d":40}
maximum = None
max_key = None
for key, value in d.items():
    if maximum is None or value > maximum:
        maximum = value
        max_key = key
print(max_key)


#Find the key with the lowest value.
d = {"a":10,"b":20,"c":30,"d":40}
minimum = None
min_key = None
for key, value in d.items():
    if minimum is None or value < minimum:
        minimum = value
        min_key = key
print(min_key)

#Sort the dictionary by keys.
d = {"c":30,"a":10,"d":40,"b":20}
for key in sorted(d):
    print(key, d[key]) 

#Sort the dictionary by values.
d = {"a":10,"b":20,"c":30,"d":40}

for key, value in sorted(d.items(), key=lambda x: x[1]):
    print(key, value)


#Remove duplicate values.
d = {"a":10,"b":20,"g":10,"c":30}
new = {}
for key, value in d.items():
    if value not in new.values():
        new[key] = value
print(new)


#Find common keys between two dictionaries.
d = {"a":1,"b":2}
x = {"b":4,"g":9}
for key in d:
    if key in x:
        print(key)


#Check if two dictionaries are equal.
d = {"a":1,"b":2}
x = {"b":4,"g":9}
print(d == x)


#Convert two lists into a dictionary.
keys = ["a","b","c"]
values = [10,20,30]
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)





