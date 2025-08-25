data_types = [
    "str", "int", "float", "complex",
    "list", "tuple", "range",
    "dict",
    "set", "frozenset",
    "bool",
    "bytes", "bytearray", "memoryview"
]
l_str = []
l_bool = []
l_dict = []
l_byte = []
l_list = []
l_set = []
for i in data_types:
    if type(i) == str:
        l_str.append(i)
    elif type(i) == bool:
        l_bool.append(i)
    elif type(i) == dict:
        l_dict.append(i)
    elif type(i) == bytes:
        l_byte.append(i)
    elif type(i) == list:
        l_list.append(i)    
    elif type(i) == set:
        l_set.append(i)

print("String Data Types: ", l_str)
print("Boolean Data Types: ", l_bool)
print("Dictionary Data Types: ", l_dict)
print("Byte Data Types: ", l_byte)
print("List Data Types: ", l_list)  
print("Set Data Types: ", l_set)
        