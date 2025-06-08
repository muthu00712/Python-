m=int(input())
n=int(input())
for i in range(m,n+1):
    if(i%4==0 and i%100!=0) or (i%400==0):
        print(i)
