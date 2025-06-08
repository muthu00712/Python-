n=input()
try:
 if n=='/':
  raise Exception("You must enter a numeric value.")
 if int(n)<=0:
  raise Exception("The length of the list must be a non-negative integer.")
 l=[]
 for i in range(int(n)):
  a=input()

 if a.isalpha():
  raise Exception("You must enter a numeric value.")
 else:
  l.append(int(a))
  avg=sum(l)/int(n)
  print(f"The average is: {avg:.2f}")
except Exception as e:
 print(f"Error:{e}")