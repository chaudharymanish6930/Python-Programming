def less_than(lst,k):
    for i in lst:
        if lst[i]<k:
            return lst[i]

print(less_than([1,-2,0,5,-3],0))

def less_than(lst,k):
    x=[i for i in lst if i<k]
    return x

print(less_than([1,-2,0,5,-3],0))