nth=int(input("how many terms?::"))
n1,n2=0,1
count=0
if nth<=0:
    print("enter a positive number")
elif nth==1:
    print(n1)
else:
    print("fibbonacci series:")
    print(n1,n2,end=" ")
    for i in range(3,nth+1):
        nth=n1+n2
        print(nth,end=" ")
        n1=n2
        n2=nth
