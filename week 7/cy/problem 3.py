# You are using Python
import numpy as np
data = [list(map(float, input().split())) for _ in range(5)]
rainfall = np.array(data)
yearly_totals = np.sum(rainfall, axis=1)
max_rainfall_months = np.argmax(rainfall, axis=1)
print(yearly_totals)
print(max_rainfall_months)