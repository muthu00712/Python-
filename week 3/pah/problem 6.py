n=input()
arr=list(map(int,input().split()))

num=1
while True:
    if num not in arr:
        print(num)
        break
    
    num+=1
