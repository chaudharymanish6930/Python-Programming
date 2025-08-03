<<<<<<< HEAD
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
ṇ
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

my_dict["country"] = "USA"  # Adding a new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

del my_dict["city"]  # Removing a key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(my_dict.values())  # Output: dict_values(['Alice', 26, 'USA'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 26), ('country', 'USA')])
=======
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
ṇ
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

my_dict["country"] = "USA"  # Adding a new key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'country': 'USA'}

del my_dict["city"]  # Removing a key-value pair
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'country': 'USA'}

print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(my_dict.values())  # Output: dict_values(['Alice', 26, 'USA'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 26), ('country', 'USA')])
>>>>>>> 85a1649 (first)
