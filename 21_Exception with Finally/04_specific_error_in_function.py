def fun1():
    try:
        l=[1,2,3,4,5]
        x=int(input("enter the index: "))
        print("element: ",l[x])
        return 1
    except ValueError:
        print("Error: value error!")
        return 0
    except IndexError:
        print("invalid indexx")
        return -1
    finally:
        print("End of the program")

y=fun1()
print("last: ",y)