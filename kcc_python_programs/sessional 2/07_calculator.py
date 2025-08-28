def calculator(x,y):
    print("1.for addition")
    print("2.for substraction")
    print("3for multiplication")
    print("4.for division")
    a=int(input("enter youur choice:"))
    if 1==a:
        return x+y
    elif 2==a:
        return x-y
    elif 3==a:
        return x*y
    elif 4==a:
        return x//y
    else:
        print("invalid input")
x=int(input("enter a nuumber:"))
y=int(input("enter another number:"))
print(calculator(x,y))