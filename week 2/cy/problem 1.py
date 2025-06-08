n=input().strip()
if n=='d' or n=='D':
    m=float(input())
    print(f"Distance: {343*m:.2f} m")
elif n=='b' or n=='B':
    m=float(input())
    print(f"Weight: {5.0*m:.2f} lb")
elif n=='f' or n=='F':
    m=float(input())
    o=float(input())
    print(f"Altitude: {m*o:.2f} m")
else:
    print("Invalid")