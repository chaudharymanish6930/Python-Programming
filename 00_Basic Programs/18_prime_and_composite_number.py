prime=[]
composite=[]
n=int(input('enter the number:'))
for i in range(1,n+1):
    if i>1:
        for j in range(2,n+1):
            if j%i==0:
                composite.append(j)
                break
            else:
                prime.append(i)
print("prime number:",prime)
print("composite number:",composite)