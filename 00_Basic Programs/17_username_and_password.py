def is_valid_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False

    # Check if the password contains a number
    if not any(char.isdigit() for char in password):
        print("Password must include at least one number.")
        return False

    # Check if the password contains an uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must include at least one uppercase letter.")
        return False

    # Check if the password contains a lowercase letter
    if not any(char.islower() for char in password):
        print("Password must include at least one lowercase letter.")
        return False

    # Check if the password contains a special character
    special_characters = "!@#$%^&*()_+[]{};:,.<>?/"
    if not any(char in special_characters for char in password):
        print("Password must include at least one special character (e.g., !, @, #).")
        return False

    return True

def main():
    print("Welcome! Please register your account.")
    username = input("Enter your username: ")
    while True:
        password = input("Enter your password: ")
        if is_valid_password(password):
            print(f"Registration successful! Welcome, {username}.")
            break
        else:
            print("Your password does not meet the requirements. Please try again.")

if __name__ == "__main__":
    main()

