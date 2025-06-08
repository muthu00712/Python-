try:
    a=float(input())
    b=int(input())


    if a<=0:

        raise ValueError("Invalid Price")
        
    if b<=0:    
        raise ValueError("Invalid Quantity")
        
        
    total=a*b
    if total>1000:
        raise RuntimeError("Excessive Cost")
        
    print(f"{total:.1f}")
    
except ValueError as ve:
    print(ve)
except RuntimeError as re:
    print(re)