m=int(input())
n=0
o=0
for i in range(1,m+1):
    if i%2==0:
        n+=i
    else:
        o+=i
    
print(f"Sum of even numbers from 1 to {m} is {n}")
print(f"Sum of odd numbers from 1 to {m} is {o}")
