#Find the sum of all values in a dictionary.
d = {"a": 10, "b": 20, "c": 30}
sum=0
for "value" in d.values():#print(sum(d.values()))
    sum+=1
print(sum)

#Find the maximum value.
d = {"a": 10, "b": 20, "c": 30}

values = list(d.values())
maximum = values[0]
for value in values:#print(max(d.values()))
    if value > maximum:
        maximum = value
print(maximum)
