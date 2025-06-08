def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
        
n= int(input())
o,p=0,1
c=0
while c<n:
    fib=o+p
    if is_prime(fib):
        print(fib,end="")
        c+=1
    o,p=p,fib

