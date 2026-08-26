#replace all digits with characters
n=input()
res=""
for i in range(len(n)):
    if n[i].isdigit():
        shift=int(n[i])
        res+=chr(ord(n[i-1])+shift)
    else:
        res+=n[i]
print(res)            

