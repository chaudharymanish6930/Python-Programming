# it is ordered but not changeable
# it is immutable
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) 
print("elephant" in animals)  

fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
fruits.add("cherry") # This will raise an error because frozensets are immutable
print(fruits) 