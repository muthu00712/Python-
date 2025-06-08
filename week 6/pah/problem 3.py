line = input().strip()
parts = line.split()
numbers = []
for part in parts:
  try:
   num = float(part)
   numbers.append(num)
  except ValueError:
   print("Invalid data in the input.")
   break
else:
 avg = sum(numbers) / len(numbers)
 print(f"Average of the numbers is: {avg:.2f}")