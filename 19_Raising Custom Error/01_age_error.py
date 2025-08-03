def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print("Valid age:", age)

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)
