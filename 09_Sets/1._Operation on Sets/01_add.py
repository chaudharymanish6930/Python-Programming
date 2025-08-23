# single element will be added in this cases 
# all type of data types in sets
s1={1,2,3}
s1.add(4)
print(s1)
#sets is mutable but set's elements are immutable 

s1.add((5,6))  # tuple can be added
print(s1)
#s1.add([7,8])  # list cannot be added
#print(s1)  