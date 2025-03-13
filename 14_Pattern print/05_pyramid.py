n=int(input("enter the value:"))
l=0
for i in range(1,n+1):
    for j in range(n-1):
            print(" ",end="")
    for k in range(2*i-1):
          print("*",end="")
    