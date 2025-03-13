# Creating a bytes object
b = bytes([65, 66, 67, 68])

# Creating a memoryview object
mv = memoryview(b)
print(mv[1])  # Output: 66 (ASCII of 'B')

# Slicing without copying data
sub_mv = mv[1:3]
print(bytes(sub_mv))  # Output: b'BC'
