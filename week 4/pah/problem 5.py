weight = float(input())
height = float(input())
def calculate_bmi(weight,height):
    c=height**2
    d=weight/c
    print(f"Your bmi is: {d:.2f}")
calculate_bmi(weight, height)