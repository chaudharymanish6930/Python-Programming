def fun(a,b,c):
    d=c+a+b
    return d
print(fun(2,3,6))

def fun1(a,b,c):
    return a,b,c
print(fun1(b=5,c=9,a=7))

def fun2(a,b,c):
    return a,b,c
# print(fun2(b=5,c=9,a=7,d=9))
# here d creates an error in this code

def fun3(a,b,c):
    return a,b,c
# print(fun3(4,7))
# in this code creates an error beacuse only tWo function call in it.


def fun4(a,b,c):
    return a,b,c
# print(fun4(b=7,6,5)) #error
print(fun4(6,b=5,c=9))
# print(fun4(7,b=8,9)) errror

