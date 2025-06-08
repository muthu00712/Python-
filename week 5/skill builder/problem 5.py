a=int(input())
b=tuple(map(int,input().strip('()').split(',')))
c=tuple(map(int,input().strip('()').split(',')))
e=[]

for i in range(a):
    e.append(b[i]+c[i])
    
print((tuple(e)))