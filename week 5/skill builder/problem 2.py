# Read number of product IDs
n = int(input())

# Initialize dictionary to store frequency
freq = {}

# Read each product ID and update frequency
for _ in range(n):
    pid = int(input())
    if pid in freq:
        freq[pid] += 1
    else:
        freq[pid] = 1

# Calculate total unique IDs
total_unique = len(freq)

# Calculate average frequency
total_occurrences = sum(freq.values())
average_freq = total_occurrences / total_unique

# Display results
print(dict(freq))

print("Total Unique IDs:", total_unique)
print("Average Frequency: {:.2f}".format(average_freq))
