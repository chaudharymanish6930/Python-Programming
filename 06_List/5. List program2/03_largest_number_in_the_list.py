li=[23,43,56,123,663,785,85,643,364]
max=li[0]
for i in li:
    if max<i:
        max=i
print(max)

# another method by sorted lsit
# sorted arrange the number in the increasing order
li.sort()  
print("the largest no:",li[-1])
print("the largest no:",li[-2])
print("the largest no:",li[-4])
print("the largest no:",li[-3])