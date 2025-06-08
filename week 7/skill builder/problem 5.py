# You are using Python
import pandas as pd
n = int(input())
cities = input().split()
months = input().split()
sales = list(map(float, input().split()))
index = pd.MultiIndex.from_tuples(zip(cities, months), names=['City', 'Month'])
df = pd.DataFrame({'Sales': sales}, index=index)
print("Monthly Sales Data with MultiIndex:")
print(df)
print("\nTotal Sales Per City:")
print(df.groupby(level='City').sum())