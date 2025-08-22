words = ["Hello,", "Python", "Programming!"]
joined_string = "-".join(words)  # Join words with a hyphen
print("Joined with '-':", joined_string)


# List of words
words = ["Apple", "Banana", "Cherry", "Date"]

# Joining with different characters
comma_joined = ", ".join(words)   # Using comma and space
space_joined = " ".join(words)    # Using space
hyphen_joined = "-".join(words)   # Using hyphen
underscore_joined = "_".join(words)  # Using underscore

# Display the results
print("Joined with Comma:", comma_joined)
print("Joined with Space:", space_joined)
print("Joined with Hyphen:", hyphen_joined)
print("Joined with Underscore:", underscore_joined)