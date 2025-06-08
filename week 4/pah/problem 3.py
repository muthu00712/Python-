num = int(input())
def digital_root(num):
    while num>=10:
        c=0
        for i in str(num):
            c+=int(i)
        num=c
    return num
print(digital_root(num))
