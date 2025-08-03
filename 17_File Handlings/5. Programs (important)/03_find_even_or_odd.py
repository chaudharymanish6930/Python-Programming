<<<<<<< HEAD
with open("D:/python/01upload on github/17_File Handlings/5. Programs (important)/03_number.txt", 'r') as file:
    content = file.read()  # Read the file content
    print("File Content:", content)

    # Split the content by comma and convert each number to an integer
    num = content.split(",")

    # Iterate through the numbers and check even or odd
    for i in num:
        i = i.strip()  # Remove extra spaces or newline characters
        if i.isdigit():  # Ensure it's a valid number
            number = int(i)
            if number % 2 == 0:
                print(f"Even: {number}")
            else:
                print(f"Odd: {number}")
=======
with open("D:/python/01upload on github/17_File Handlings/5. Programs (important)/03_number.txt", 'r') as file:
    content = file.read()  # Read the file content
    print("File Content:", content)

    # Split the content by comma and convert each number to an integer
    num = content.split(",")

    # Iterate through the numbers and check even or odd
    for i in num:
        i = i.strip()  # Remove extra spaces or newline characters
        if i.isdigit():  # Ensure it's a valid number
            number = int(i)
            if number % 2 == 0:
                print(f"Even: {number}")
            else:
                print(f"Odd: {number}")
>>>>>>> 85a1649 (first)
