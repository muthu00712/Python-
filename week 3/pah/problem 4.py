a=int(input())
b=[]
for i in range(a):
    c=int(input())
    b.append(c)

b.sort()
print(f"Original List: {b}")

d=[]

for i in range(a):
    if i==0:
        d.append(0)
    elif i%2==0:
        d.append(b[i]**3)
    else:
        d.append(b[i]**2)
        
print(f"Replaced List: {d}")