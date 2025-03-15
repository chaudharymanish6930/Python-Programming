def fun1():
    try:
        l=[1,2,3,4,5]
        index=int(input("Enter the index: "))
        print("Element:",l[index])
        return 1
    except:
        print("Error: Invalid index!")
        return 0
    finally:
        print("End of the program")
x= fun1()
print("last: ",x)