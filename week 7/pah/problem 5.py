# You are using Python
import numpy as np
rows, cols = map(int, input().split())
data = [list(map(float, input().split())) for _ in range(rows)]
returns = np.array(data)
positive_days = np.all(returns > 0, axis=1)
print("Days where all asset returns were positive:")
print(positive_days)