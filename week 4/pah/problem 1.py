m=int(input())
lst=list(map(int,input().split()))

c=list(filter(lambda x: x%3==0,lst))
d=list(filter(lambda x:x%5==0,lst))

print(len(c))
print(len(d))
print(sum(c))
print(sum(d))