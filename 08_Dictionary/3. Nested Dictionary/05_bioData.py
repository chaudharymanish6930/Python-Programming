d7 = {
    "name": "John",
    "age": 30,
    "Email address":"me.developer@gmail.com",
    "address": {
        "city": "New York",
        "state": "NY",
        "zip": "10001"
    },
    "Subjects": ["Math", "Science", "English"]   
}
print(d7["address"]["city"])  # Accessing nested dictionary value
print(d7["Subjects"][1])      # Accessing list element inside dictionary
print(d7)