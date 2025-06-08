a=set(map(int,input().split()))
b=set(map(int,input().split()))
c=set(map(int,input().split()))

d=a&b
e=d-c
print(d)
print(e)