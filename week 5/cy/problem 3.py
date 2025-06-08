# Read number of sets
k = int(input())

# Read all sets into a list
sets = []
for _ in range(k):
    elements = set(map(int, input().split()))
    sets.append(elements)

# Perform symmetric difference step-by-step and print intermediate results
result = sets[0]
for s in sets[1:]:
    result = result.symmetric_difference(s)
    print(list(s.symmetric_difference(result)))  # Print current operation's difference

# Final result
print(list(result))
