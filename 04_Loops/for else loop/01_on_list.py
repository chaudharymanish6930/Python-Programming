x=[12,21,32,121,42,32]
for i in x:
    print(i," ",end="")  # prints all the elements of list one by one
    if i==121:
        print("\n121 is found in the list")
        break   
else:
    print("\n121 is not found in the list")

# The else block will execute only if the loop is not terminated by a break statement