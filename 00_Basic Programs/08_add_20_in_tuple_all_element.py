t1=(10,11,12,13,14)
li=list(t1)
print(li)
print(type(li))
for i in range(len(li)):
    li[i]=li[i]+20
new_t1=tuple(li)
print(new_t1)