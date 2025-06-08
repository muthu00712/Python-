# You are using Python
import numpy as np
def mul5(n):
 arr=np.zeros(n)
 s=input()
 s1=s.split()
 for i in range(n):
  if(int(float(s1[i]))%5==0 and int(float(s1[i]))>100):
   arr[i]=s1[i]

 arr2=arr[(arr>0)]


 return arr2
n=int(input())
print(mul5(n))