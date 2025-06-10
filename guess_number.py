import random  # to generate a random number
import time  # to track the timer
import threading  # to manage the timer in a separate thread


# Function to handle the timer
def time_limit():
    print("You have 10 seconds to make a guess!")
    time.sleep(10)  # Wait for 10 seconds
    print("\nTime's up! You took too long to guess.")
    return False


# Function to start the game
def guess_number():
    # Select difficulty level
    print("Choose a difficulty level:")
    print("1. Easy (1 to 10)")
    print("2. Hard (1 to 100)")
    difficulty = input("Enter 1 for Easy or 2 for Hard: ").strip()

    if difficulty == '1':
        secret_number = random.randint(1, 10)  # Easy mode (1-10)
    else:
        secret_number = random.randint(1, 100)  # Hard mode (1-100)

    # Maximum number of guesses allowed
    max_guesses = 3
    score = 0

    print(f"Hello! I've picked a number between 1 and {'10' if difficulty == '1' else '100'}.")
    print(f"You have {max_guesses} attempts to guess the correct number.")

    for attempt in range(1, max_guesses + 1):
        print(f"\nAttempt {attempt}:")

        # Start timer in a separate thread
        timer_thread = threading.Thread(target=time_limit)
        timer_thread.start()

        # Ask for the guess and record the time
        start_time = time.time()  # start the timer

        # Input validation: Ensure the player inputs a valid number
        while True:
            guess_input = input("Enter your guess: ").strip()

            # If input is empty or non-numeric, ask the player to enter again
            if not guess_input.isdigit():
                print("Invalid input! Please enter a valid number.")
                continue  # Skip this iteration and ask again
            guess = int(guess_input)
            break  # Exit the loop once a valid number is entered

        elapsed_time = time.time() - start_time  # measure time taken for input

        # If the guess took too long, end the game
        if elapsed_time > 10:
            print("Game Over! Time's up!")
            break

        # Stop the timer thread if the player guesses before time runs out
        timer_thread.join()

        # Check if the guess is correct, too low, or too high
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You guessed the correct number on attempt {attempt}!")
            if attempt == 1:
                score = 3
            elif attempt == 2:
                score = 2
            else:
                score = 1
            break
    else:
        print(f"Sorry, you're out of attempts. The correct number was {secret_number}.")

    print(f"Your final score: {score} points.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_number()  # Call the function to start a new game
    else:
        print("Thanks for playing!")


# Start the game
guess_number()