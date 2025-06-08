# You are using Python
import pandas as pd
import io
n = int(input())
header = input()
lines = [input() for _ in range(n)]
csv_data = header + '\n' + '\n'.join(lines)
df = pd.read_csv(io.StringIO(csv_data))
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fllna(mean_age)
df = df.dropna(subset=['Diagnosis']).reset_index(drop=True)
print("Cleaned Hospital Records:")
print(df)