# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Read input
n = int(input())

# Generate the dictionary
prime_dict = {}
count = 0
current = 2

while count < n:
    if is_prime(current):
        count += 1
        prime_dict[count] = current
    current += 1

# Print the dictionary
print(prime_dict)
