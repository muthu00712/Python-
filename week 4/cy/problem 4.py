a=list(map(int,input().split()))
c=[]
for i in a:
    if i%2==0:
        c.append(i)
      
if c:
    
    print(f"The maximum even price is: {max(c)}")
else:
    print("No even prices were found")