#add two str without int directly usage
n1=input()
n2=input()
res=""
carry=0
i=len(n1)-1
j=len(n2)-1
while i>=0 or j>=0 or carry:

   d1=int(n1[i]) if i>=0 else 0
   d2=int(n2[j])if j>=0 else 0
   total=d1+d2+carry
   carry=total//10
   res=str(total%10)+res
   i-=1
   j-=1
print(res)


