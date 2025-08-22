import math
def p(n):
    temp = n
    a = math.sqrt(n)
    if(n==a**2):
        return True
    else:
        False
n=int(input("Enter a Number: "))
if(p(n)):
    print("Yes, it is a Perfect Square",n)
else:
    print("No, it's not -1")
