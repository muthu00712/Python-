# You are using Python
# Read number of tuples
N = int(input())

# Initialize list to store all quantities
all_quantities = []

# Read N tuples
for _ in range(N):
    # Read line and evaluate it as a tuple (e.g., (1, [3, 4]))
    item = eval(input())  # e.g., (1, [3, 4])
    quantities = item[1]  # Get the list of quantities
    all_quantities.extend(quantities)  # Add to the combined list

# Read the threshold
threshold = int(input())

# Use filter to get quantities greater than the threshold
filtered = list(filter(lambda x: x > threshold, all_quantities))

# Print result space-separated
print(*filtered)
