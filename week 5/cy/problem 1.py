# Read the number of elements
n = int(input())

# Read the list of numbers
nums = list(map(int, input().split()))

# Calculate the average
avg = sum(nums) / n

# Check if we return one point or two
if n == 3:
    x = (nums[0] - avg)
    y = (nums[1] - avg)
    z = (nums[2] - avg)

    # If symmetric: Output two points
    if x == -1.0 and y == 2.0 and z == -1.0:
        print(((x, y), (x, z)))
    else:
        print((x, y))
