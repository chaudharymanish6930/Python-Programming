x="manish choudhary"
y=x[-1]+x[1:-1]+x[0]
print(y)
print(x[1:-1])

def swap(y):
    if len(y)<=1:
        return y
    return y[-1]+y[1:-1]+y[0]
z=input("enter a string:")
new_string=swap(z)
print(f"modified string:{new_string}")
