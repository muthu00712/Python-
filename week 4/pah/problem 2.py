num = int(input())

def sum_digits(num):

    c=0
    for i in str(num):
        c+=int(i)
    return c

sum = sum_digits(num)
print(sum)