# You are using Python
import pandas as pd
n = int(input())
data = [input().split() for _ in range(n)]
df = pd.DataFrame(data, columns=["Product_ID", "Quantity"])
df["Quantity"] = df["Quantity"].astype(int)
zero_stock = df[df["Quantity"] == 0]
print("Products with Zero Stock:")
if zero_stock.empty:
 print("No products with zero stock.")
else:
 print(zero_stock.to_string(index=False))