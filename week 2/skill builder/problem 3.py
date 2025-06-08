m=int(input())
n=int(input())
sum=0
for i in range(m,n+1):
    k=str(abs(i))
    o=int(k[0])
    p=int(k[-1])
    if o==p:
        continue
    sum+=o+p
print(sum)
