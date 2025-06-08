import numpy as np
sensors, samples = map(int, input().split())
data = [list(map(float, input().split())) for _ in range(sensors)]
arr = np.array(data)
means = np.mean(arr, axis=1, keepdims=True)
stds = np.std(arr, axis=1, keepdims=True)
normalized = (arr - means) / stds
print("Normalized Sensor Data:")
print(normalized)