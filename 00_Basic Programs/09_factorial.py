num=int(input("enter the lenght of sreies:"))
factorial=1
if num<0:
    print("the factorial don't exist")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):  # 5 for example
        factorial=factorial*i
    print("the factorail of",num,"is",factorial)
