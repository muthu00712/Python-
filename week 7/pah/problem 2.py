# You are using Python
import numpy as np
rows = int(input())
cols = int(input())
matrix = [list(map(int, input().split())) for _ in range(rows)]
image = np.array(matrix, dtype=float)
min_pixel = image.min()
max_pixel = image.max()
if min_pixel == max_pixel:
 normalized_image = np.zeros_like(image)
else:
 normalized_image = (image - min_pixel) / (max_pixel - min_pixel)
print(normalized_image)