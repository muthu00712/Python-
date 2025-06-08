m=str(input())
v="A,E,I,O,U,a,e,i,o,u"
result=""
for i in m:
    if not i.isalpha():
        continue
    if i in v:
        continue
    result+=i+""
    
    
print(result)