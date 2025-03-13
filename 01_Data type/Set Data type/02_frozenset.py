# it is ordered but not changeable
# it is immutable
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) 
print("elephant" in animals)  

fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
fruits.add("cherry") # not possible
print(fruits) 