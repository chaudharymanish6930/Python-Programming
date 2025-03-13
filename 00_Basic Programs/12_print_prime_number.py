lower=int(input("enter a number: "))
upper=int(input("enter another number: "))
print("the prime number from",lower,"to",upper)
for num in range(lower,upper):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)