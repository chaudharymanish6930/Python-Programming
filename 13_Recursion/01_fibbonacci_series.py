# f0=0
# f1=1
# f2=f1+f0
# fn= (fn-1)+(fn-2)

def Fibonacci(a):
    x = 0
    y = 1
    while(x < a):
        print(x)
        z = x
        x = y
        y = z + y
        
a = int(input("Enter the number till which you want your Fibonacci series: "))

Fibonacci(a)