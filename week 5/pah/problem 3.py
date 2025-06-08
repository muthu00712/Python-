# Read input
n = int(input())

# Generate the dictionary using dictionary comprehension
square_dict = {i: i**2 for i in range(1, n+1)}

# Print the dictionary
print(square_dict)
