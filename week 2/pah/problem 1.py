def collatz_steps(n):
    m=0
    while n!=1 and m<=100:
        
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        m+=1
    
    if m>100:
        print("Exceeded 100 steps. Exiting...")
    else:
        print(f"Steps taken to reach 1: {m}")
n=int(input())
collatz_steps(n)