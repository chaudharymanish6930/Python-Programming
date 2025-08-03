<<<<<<< HEAD
# it is ordered but not changeable
# it is immutable
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) 
print("elephant" in animals)  

fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
fruits.add("cherry") # not possible
=======
# it is ordered but not changeable
# it is immutable
animals = frozenset(["cat", "dog", "lion"])
print("cat" in animals) 
print("elephant" in animals)  

fruits = frozenset(["apple", "banana", "orange"])
print(fruits) 
fruits.add("cherry") # not possible
>>>>>>> 85a1649 (first)
print(fruits) 