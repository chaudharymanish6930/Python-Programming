<<<<<<< HEAD
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10. You have 5 attempts.")

# Allow the user 5 attempts
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    # Conditional checks
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts!")
        break  # Exit loop if guessed correctly
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If the user couldn't guess in 5 attempts
else:
    print(f"❌ Sorry, you've used all attempts. The correct number was {secret_number}. Better luck next time!")
=======
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10. You have 5 attempts.")

# Allow the user 5 attempts
for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    # Conditional checks
    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number {secret_number} correctly in {attempt} attempts!")
        break  # Exit loop if guessed correctly
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

# If the user couldn't guess in 5 attempts
else:
    print(f"❌ Sorry, you've used all attempts. The correct number was {secret_number}. Better luck next time!")
>>>>>>> 85a1649 (first)
