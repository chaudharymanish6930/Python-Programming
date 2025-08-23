s3={1,2,3,3,54,"manish"}
s3.remove("manish") # shows erroe in this case if the elemneti s not present in the given sets

# both same
s3.discard(2)
print(s3)

# diffrence between remove and discard
s3.remove(100) # shows erroe in this case if the elemneti s not present in the given sets

s3.discard(100)  # does not show error if the element is not present in the given set
print(s3)