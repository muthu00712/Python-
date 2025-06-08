import numpy as np
import math
n = int(input())
wait_times = list(map(float, input().split()))
data = np.array(wait_times)
max_time = data.max()
bucket_end = math.ceil(max_time / 5) * 5
bins = np.arange(0, bucket_end + 5, 5)
# Use digitize with right=False for [lower, upper)
bucket_indices = np.digitize(data, bins, right=False)
print("Wait Time Buckets and Counts:")
for i in range(1, len(bins)):
 count = np.sum(bucket_indices == i)
 if count > 0:
  print(f"{int(bins[i-1])}-{int(bins[i])}: {count}")