n=int(input("enter the nuumber:"))
num=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n*n//10
print("reverse",rev)
if rev==num:
    print("palidrome")
else:
    print("not palidrome")