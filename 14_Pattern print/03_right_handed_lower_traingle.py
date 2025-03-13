x=int(input("enter the length:"))
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=i-1:
            print(" ",end="")
        else:
            print("*",end="")
    print("\n")