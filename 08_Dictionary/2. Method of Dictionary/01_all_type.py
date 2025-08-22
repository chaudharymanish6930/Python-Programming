# Creating a dictionary
my_dict = {"apple": 3, "banana": 5}

# Accessing keys and values
print(my_dict.keys())         # dict_keys(['apple', 'banana'])
print(my_dict.values())       # dict_values([3, 5])

# Updating and adding items
my_dict.update({"cherry": 7})
print(my_dict)                # {'apple': 3, 'banana': 5, 'cherry': 7}

# Removing items
my_dict.pop("banana")
print(my_dict) 
