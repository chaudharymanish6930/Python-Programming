x=float(input("enter the value of x:"))
y=float(input("enter the value of y:"))
z=float(input("enter the operands{+,-,*,/,%,//}  "))
if z=="+":
    print("the sum of two number:",x+y)
elif z=="-":
    print("the substraction of two number:",x-y)
elif z=="*":
    print("the multiplication of two number:",x*y)
elif z=="/":
    print("the divisible of two number:",x/y)
elif z=="%":
    print("the modulus of two number:",x%y)
elif z=="//":
    print("the floor of two number:",x//y)
else:
    print("you want nothing")