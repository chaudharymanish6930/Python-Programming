# Demonstration of various built-in functions in Python

# abs()
print("abs(-5):", abs(-5))

# all()
print("all([True, True, False]):", all([True, True, False]))

# any()
print("any([False, False, True]):", any([False, False, True]))

# bin()
print("bin(10):", bin(10))

# bool()
print("bool(0):", bool(0))

# chr()
print("chr(65):", chr(65))

# divmod()
print("divmod(9, 2):", divmod(9, 2))

# enumerate()
for idx, val in enumerate(['a', 'b', 'c']):
    print(f"enumerate: {idx} -> {val}")

# filter()
def is_even(n):
    return n % 2 == 0
print("filter(is_even, [1,2,3,4]):", list(filter(is_even, [1,2,3,4])))

# float()
print("float('3.14'):", float('3.14'))

# int()
print("int('7'):", int('7'))

# len()
print("len('hello'):", len('hello'))

# list()
print("list('abc'):", list('abc'))

# map()
print("map(str.upper, ['a','b']):", list(map(str.upper, ['a','b'])))

# max()
print("max([1, 2, 3]):", max([1, 2, 3]))

# min()
print("min([1, 2, 3]):", min([1, 2, 3]))

# pow()
print("pow(2, 3):", pow(2, 3))

# range()
print("list(range(3)):", list(range(3)))

# reversed()
print("list(reversed([1,2,3])):", list(reversed([1,2,3])))

# round()
print("round(3.14159, 2):", round(3.14159, 2))

# sorted()
print("sorted([3,1,2]):", sorted([3,1,2]))

# str()
print("str(123):", str(123))

# sum()
print("sum([1,2,3]):", sum([1,2,3]))

# type()
print("type(123):", type(123))

# zip()
print("list(zip([1,2],[3,4])):", list(zip([1,2],[3,4])))