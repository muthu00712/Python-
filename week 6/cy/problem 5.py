# You are using Python
n1=float(input())
n2=int(input())
try:
 if n1<=0:
  raise ValueError("Invalid Price")
 if (n1*n2)>1000:
  raise RuntimeError("Excessive Cost")
 if n2<=0:
  raise ValueError("Invalid Quantity")
 n3=n1*n2
 print(f"{n3:.1f}")
except ValueError as e:
 print(e)
except RuntimeError as r:
 print(r)