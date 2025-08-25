d1 ={
    [1,2,3] : "List as a key",
}
#  it shows an error because list is mutable

d2 ={
    (1,2,3) : "Tuple as a key"
}
# it works because tuple is immutable
print(d2)
d3 ={
    {1,2,3} : "Set as a key"
}
#  it shows an error because set is mutable
print(d3)
d4 ={
    {13:"value"} : "Frozenset as a key"
}
# it works because frozenset is immutable
print(d4)

# key in dictionary must be immutable