a=input()
c=0
d=0
f=0
g=0
for i in a:
    if i.isupper():
        c+=1
    elif i.islower():
        d+=1
    elif i.isdigit():
        f+=1
    else:
        g+=1
        
print(f"Uppercase letters: {c}")
print(f"Lowercase letters: {d}")
print(f"Digits: {f}")
print(f"Special characters: {g}")