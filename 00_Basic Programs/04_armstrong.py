<<<<<<< HEAD
n=int(input("enter the numbber:"))
sum=0
num=n
while n>0:
    digit=n%10      # last digit milegi
    sum +=digit**3
    n//=10       # last digit hategi
if num==sum:
    print("it is an armstrong number")
else:
=======
n=int(input("enter the numbber:"))
sum=0
num=n
while n>0:
    digit=n%10      # last digit milegi
    sum +=digit**3
    n//=10       # last digit hategi
if num==sum:
    print("it is an armstrong number")
else:
>>>>>>> 85a1649 (first)
    print("it is not an armstrong number")