y=input("Enter a number: ")
print("Multiplication table...")

try:
    for i in range(1,11):
        print(f"{int(y)} X {i} = {int(y)*i}")
        
except Exception as e:
    print(f"Error: {e}")
    print("Sorry some error occuered")

print("End of the program")
