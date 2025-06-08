try:
    n = input()
    if not n.lstrip('-').isdigit():
        print("Error: You must enter a numeric value.")
    else:
        n = int(n)
        if n <= 0:
            print("Error: The length of the list must be a non-negative integer.")
        else:
            total = 0
            for _ in range(n):
                val = input()
                if not val.lstrip('-').isdigit():
                    print("Error: You must enter a numeric value.")
                    break
                total += int(val)
            else:
                avg = total / n
                print(f"The average is: {avg:.2f}")
except:
    print("Error: You must enter a numeric value.")
