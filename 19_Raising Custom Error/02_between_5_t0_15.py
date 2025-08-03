a=int(input("enter a number between 5 to 15: "))

if a<5 or a>15:
    raise ValueError("Error: Number is not in the range of 5 to 15")
