import numpy as np
products, months = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(products)]
sales_array = np.array(data)
cumulative_array = np.cumsum(sales_array, axis=1)
print("Cumulative Monthly Sales:")
print(cumulative_array)