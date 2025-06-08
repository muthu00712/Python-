# Read number of elements
n = int(input())

# Read the elements and convert them to a list of integers
elements = list(map(int, input().split()))

# Create list of pairs
pairs = []
for i in range(n):
    if i < n - 1:
        pairs.append((elements[i], elements[i+1]))
    else:
        pairs.append((elements[i], None))

# Convert to tuple and print
print(tuple(pairs))
