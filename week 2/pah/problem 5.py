m=int(input())
p=0
if m>200:
   p+=(m-200)*10
   m=200
if m>100:
    p+=(m-100)*5
print(f"Rs. {p}")