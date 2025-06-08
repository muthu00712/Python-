# Read space-separated integers from input
numbers = list(map(int, input().split()))

# Create a list to store unique elements while preserving order
unique_numbers = []
seen = set()

for num in numbers:
    if num not in seen:
        unique_numbers.append(num)
        seen.add(num)

# Concatenate the unique numbers into a single string
result = ''.join(map(str, unique_numbers))

# Print the result
print(result)
