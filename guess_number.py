import random

# Function to start the game
def guess_number():
    # Difficulty level selection
    print("Choose a difficulty level:")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    difficulty = input("Enter the number corresponding to your difficulty choice: ").strip()

    if difficulty == '1':
        range_min, range_max = 1, 10
        max_guesses = 5
        points = [5, 4, 3, 2, 1]  # Points for Easy mode
    elif difficulty == '2':
        range_min, range_max = 1, 50
        max_guesses = 10
        points = [10, 8, 6, 5, 4, 3, 2, 1, 0, 0]  # Points for Medium mode
    elif difficulty == '3':
        range_min, range_max = 1, 100
        max_guesses = 20
        points = [15, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0]  # Points for Hard mode
    else:
        print("Invalid choice, setting to Easy by default (1 to 10).")
        range_min, range_max = 1, 10
        max_guesses = 5
        points = [5, 4, 3, 2, 1]  # Default points for Easy mode

    # Secret number to guess
    secret_number = random.randint(range_min, range_max)
    score = 0

    print(f"\nYou've chosen {['Easy', 'Medium', 'Hard'][int(difficulty)-1]} mode.")
    print(f"The number is between {range_min} and {range_max}. You have {max_guesses} attempts to guess the correct number.")

    for attempt in range(1, max_guesses + 1):
        print(f"\nAttempt {attempt}:")

        # Get player's guess
        guess_input = input(f"Enter your guess: ").strip()

        if not guess_input.isdigit():
            print("Invalid input! Please enter a valid number.")
            continue  # Skip this attempt if input is invalid

        guess = int(guess_input)

        # Check if the guess is correct, too low, or too high
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the correct number on attempt {attempt}!")
            score = points[attempt - 1]  # Assign score based on the attempt number
            break  # Exit the loop if the player guesses correctly

    else:  # If the player didn't guess correctly within the attempts
        print(f"Sorry, you're out of attempts. The correct number was {secret_number}.")
        score = 0  # Set score to 0 if no correct guess

    print(f"Your final score: {score} points.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_number()  # Recursively start the game again
    else:
        print("Thanks for playing!")

# Start the game
guess_number()
