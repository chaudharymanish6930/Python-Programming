def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old!")
    else:
        print("You are eligible.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Error:", e)
