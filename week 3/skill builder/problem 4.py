# You are using Python
m=eval(input())
neg=[i for i in m if i<0]
pos=[i for i in m if i>=0]
result=neg+pos

print(f"List={result}")