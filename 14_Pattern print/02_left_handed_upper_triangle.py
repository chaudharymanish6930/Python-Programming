x=int(input("enter the length of triangle:"))
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=i:
            print(" ",end="")
        else:
            print("#",end="")
    print("\n")