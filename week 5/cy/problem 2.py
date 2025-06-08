# Read number of sets
k = int(input())

# Read all sets into a list
sets = []
for _ in range(k):
    elements = set(map(int, input().split()))
    sets.append(elements)

# Find symmetric difference across all sets
sym_diff = sets[0]
for s in sets[1:]:
    sym_diff = sym_diff.symmetric_difference(s)

# Sort the symmetric difference
sorted_diff = sorted(sym_diff)

# Print the result
print(sorted_diff)
print(sum(sorted_diff))
