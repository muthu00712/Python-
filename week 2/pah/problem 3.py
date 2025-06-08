m=int(input())
n=int(input())
c=0
for i in range(m,n+1):
    if i%3==0:
        continue
    c+=i
        
print(c)
    
