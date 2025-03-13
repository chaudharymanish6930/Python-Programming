# f0=0
# f1=1
# f2=f1+f0
# fn= (fn-1)+(fn-2)

def function(n):
    if (n==0 ):
        return 0
    elif(n==1):
        return 1
    else:
        return  function(n-1)+function(n-2)
        
n=int(input("enter a number"))
# print("the fabbonacci series :"n)





