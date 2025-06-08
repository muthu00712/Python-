m=int(input())
n=int(input())
a,b=0,1
o=set()
while a<=n:
    o.add(a)
    a,b=b,a+b
    count=0
for i in range(m,n+1):
    if i in o:
        continue
    count+=1
    
print(count)
