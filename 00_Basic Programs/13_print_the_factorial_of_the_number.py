def find_factorial(n):
    factorial=1
    for i in range(1,n+1):
        factorial*=1
        return factorial
num=int(input("enter a number too find its factorial:"))
print("the factorial of",num,"is",find_factorial(num))