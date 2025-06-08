
arr = list(map(int, input().split()))


peaks = [arr[i] for i in range(len(arr)) if 
         (i == 0 and arr[i] > arr[i + 1]) or             # First element is a peak
         (i == len(arr) - 1 and arr[i] > arr[i - 1]) or   # Last element is a peak
         (0 < i < len(arr) - 1 and arr[i] > arr[i - 1] and arr[i] > arr[i + 1])]  # Middle elements are peaks


print("Peaks:", peaks)
