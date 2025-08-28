l=[1,2,3,4,5,6,7,8,9]
# Q1.
print(l[-1:-9:-1])
print(l[-1:0:-1])
# Q2.
print(l[2:8])
print(l[-7:-1])
# Q3.
m=[x for x in l if x%2==0]
print(m)
# Q4.
mid=len(l)//2
print(l[mid:])
# Q4.
print(l[mid::-1])
l[:mid]=l[:mid][::-1]
print(l)
# Q5.
for i in l:
    y=l[i]%2
    print(y ,end=" ")
