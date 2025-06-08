a=int(input())
sum1=0
for i in range(4):
    sum1+=(a+i)**4
c=sum1/4
d=a*(a+3)
e=c-d
print("constant value: ",e)
