m=int(input())
if m==1:
    n=float(input())
    if n<50:
        print("Priority: High")
    else:
        print("Priority: Low")
elif m==2:
    n=float(input())
    if n>80:
        print("Priority: High")
    else:
        print("Priority: Low")
elif m==3:
    n=float(input())
    if n>80:
        print("Priority: High")
    else:
        print("Priority: Low")
else:
  print("Invalid")
