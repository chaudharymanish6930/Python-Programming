x=(input("enter the number: "))
print("mutltiplication table...")
try:
    for i in range(1,11):
        print(f"{int(x)} X {i} = {int(x)*i}")
except:  
    print("invalid input")


print("end of the program")