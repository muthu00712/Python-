# You are using Python
import pandas as pd
n = int(input())
data = []
for _ in range(n):
 name, years = input().split()
 data.append([name, float(years)])
df = pd.DataFrame(data, columns=["Name", "Years at Company"])
def classify(years):
 if years < 3:
  return "Junior"
 elif 3 <= years < 6:
  return "Mid"
 else:
  return "Senior"
df["Experience Level"] = df["Years at Company"].apply(classify)
print("Employee Data with Experience Level:")
print(df.to_string(index=False))