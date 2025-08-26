try:
    numbers = [1, 2, 3]
    index = int(input("Enter an index: "))
    print("Number:", numbers[index])
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Please enter a valid integer index!")

print("End of the program")