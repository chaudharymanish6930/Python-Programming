tupp =(11,24,11,3442,34,"green",46, True,False)
print(type(tupp),tupp)
print(len(tupp))

print(tupp[0])
print(tupp[1])
print(tupp[2])
print(tupp[0:2:2])
print(tupp[0:2])
print(tupp[2:8:])

if 3442 in tupp:
    print("yes 342 is present in this tuple")
else:
    print("no")