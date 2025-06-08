
m=int(input())
n=[]
for i in range(m):
    val=int(input())
    n.append(val)
    
o=int(input())
print(f"List after appending elements: {n}")
q=n.pop(o)
print(f"List after popping last element: {n}")
print(f"Popped element: {q}")