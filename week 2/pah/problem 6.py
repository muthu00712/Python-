def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
        
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
    
n=int(input())
for i in range(1,n+1,2):
    fact=factorial(i)
    digit_sum=sum_of_digits(fact)
    print(f"{i}! = {fact}, sum of digits = {digit_sum}")