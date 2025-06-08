def armstrong_number(number):
    a=str(number)   
    b=len(a) 
    c=sum(int(digit)**b for digit in a) 

    if c==number:
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an armstrong number.")

d=int(input())
armstrong_number(d)