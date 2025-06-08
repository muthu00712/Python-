a=int(input())
b={}

for i in range(a):
    c=list(map(int,input().split()))
    
    d=c[0]
    e=c[1:]
    f=sum(e)
    g=max(e)

    b[d]=[f,g]
print(b)