def search_many(s,x,k):
    return s.count(x)<=k

print(search_many([10,17,15,12,15],15,2))
print(search_many([10,12,12,12,12],12,2))
print(search_many([10,12,15,11,17],17,1))