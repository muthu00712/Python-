# You are using Python
import pandas as pd
import sys
import io
n = int(input())
header = input()
rows = [input() for _ in range(n)]
csv_data = header + '\n' + '\n'.join(rows)
df = pd.read_csv(io.StringIO(csv_data))
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], errors='coerce')
df['Purchase Month'] = df['Purchase Date'].dt.month
df['Purchase Day'] = df['Purchase Date'].dt.day
print("Transformed E-commerce Transaction Data:")
print(df)