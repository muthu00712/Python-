try:
    a=int(input())
    if a<18:
        raise ValueError("Not eligible to vote")
    if a>=18:
        raise ValueError("Eligible to vote")
        
except ValueError as ve:
    print(ve)