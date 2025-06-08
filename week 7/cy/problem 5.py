# You are using Python
import numpy as np
n = int(input())
readings = list(map(float, input().split()))
data = np.array(readings).reshape(-1, 24)
avg_per_day = np.mean(data, axis=1)
print(avg_per_day)