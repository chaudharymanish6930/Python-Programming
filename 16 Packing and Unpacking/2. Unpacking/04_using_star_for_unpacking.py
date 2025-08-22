data = (10, 20, 30, 40, "manish", 50)
a, *b, c = data  # First and last values assigned separately, rest stored in b
print(a)  # Output: 10
print(b)  # Output: [20, 30, 40]   list form

print(c)  # Output: 50