a=int(input())
b=[2,3,5,7]

divisors=list(filter(lambda x:a%x==0,b))

if divisors:
    print(f"The smallest positive divisor of {a} is: {min(divisors)}")
else:
    print("No divisors found")

