m=int(input())
n=int(input())
o=(m*8)//n
a=o//3600
b=(o%3600)//60
c=o%60
print(f"Download Time: {a} hours, {b} minutes, and {c} seconds")