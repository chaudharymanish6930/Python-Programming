person = {"name": "Alice", "age": 25, "city": "New York"}

# Loop through keys
for key in person:
    print(key)

# Loop through values
for value in person.values():
    print(value)

# Loop through both keys and values
for key, value in person.items():
    print(f"{key}: {value}")