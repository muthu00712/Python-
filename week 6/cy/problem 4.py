try:
 n=int(input())
 if n>=18:
  print("Eligible to vote")
 else:
  raise Exception("Not eligible to vote")
except Exception as e:
 print(e)