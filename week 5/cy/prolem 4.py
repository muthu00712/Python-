# Read number of elements
n = int(input())

# Read the tuple of pixel intensities
pixels = tuple(map(int, input().split()))

# Compute absolute differences between consecutive elements
differences = tuple(abs(pixels[i] - pixels[i+1]) for i in range(n - 1))

# Print the resulting tuple
print(differences)
