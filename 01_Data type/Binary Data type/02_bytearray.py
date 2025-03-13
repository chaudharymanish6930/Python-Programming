# Creating a bytearray object
ba = bytearray([65, 66, 67, 68])  # 'A', 'B', 'C', 'D'
print(ba)        # Output: bytearray(b'ABCD')

# Modifying a byte
ba[0] = 70       # Changing 'A' (65) to 'F' (70)
print(ba)        # Output: bytearray(b'FBCD')
