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





