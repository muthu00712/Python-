def is_prime(digit):
    return digit in {2,3,5,7}
m=int(input())
n=0
while m>0:
    digit=m%10
    if not is_prime(digit):
        n+=digit
    m//=10
print(n)