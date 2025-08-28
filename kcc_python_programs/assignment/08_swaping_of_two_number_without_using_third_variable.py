# Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("\nBefore swapping:")
print("num1 =", num1)
print("num2 =", num2)

# Swapping without using a third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("\nAfter swapping:")
print("num1 =", num1)
print("num2 =", num2)
