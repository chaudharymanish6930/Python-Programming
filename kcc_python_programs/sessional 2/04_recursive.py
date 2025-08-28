def rprint(lst):
    if lst:
     print(lst[-1],end="")
     rprint(lst[:-1])
rprint([1,2,3,4])
