my_list = [3, 1, 4, 1, 5, 9]
my_list.append(2)      # Adds 2 at the end
print(my_list)         # Output: [3, 1, 4, 1, 5, 9, 2]

my_list.insert(2, 8)   # Insert 8 at index 2
print(my_list)         # Output: [3, 1, 8, 4, 1, 5, 9, 2]

my_list.remove(1)      # Removes first occurrence of 1
print(my_list)         # Output: [3, 8, 4, 1, 5, 9, 2]

print(my_list.pop())   # Removes and returns last item (Output: 2)

my_list.sort()
print(my_list)         # Output: [1, 3, 4, 5, 8, 9]