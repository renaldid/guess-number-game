# **Guess Number Game**
## **Overview**
The Guess Number Game is an interactive Python-based game where the player attempts to guess a randomly chosen number by the computer. Players are given a limited number of attempts to guess the number, and they must do so within a time limit for each attempt. The game offers an adjustable difficulty level and tracks the player's performance with scoring.

This project demonstrates Python fundamentals such as loops, conditionals, input validation, multithreading, and timing. It is a fun and engaging way to practice basic programming concepts.

## **Features**
* Difficulty Levels: Choose between Easy (1-10) or Hard (1-100) difficulty.
* Timer: Players have 10 seconds to guess the number before time runs out. If they fail, the game ends immediately.
* Attempts Limit: Players can make up to 3 guesses per round.
* Scoring: The score depends on how quickly the player guesses the number:

    * 3 points for the first attempt
    * 2 points for the second attempt
    * 1 point for the third attempt
* Replay Option: After the game ends, players can choose to play again.

## **Installation**
To run this game, you will need to have Python installed on your system.
### Prerequisites
1. **Install Python**:
   - Download and install Python from the official [Python website](https://www.python.org/downloads/).
   
2. **Clone the repository**:
   You can clone the repository to your local machine using Git:
   ```bash
   git clone https://github.com/renaldid/guess-number-game.git

## **Usage**
1. Navigate to the project directory:
    * Open a terminal or command prompt.
    * Navigate to the directory where you cloned the project.
2. Run the game:
    ```bash
    python guess_number.py
3. Play the Game:
    * Follow the on-screen prompts to select a difficulty level.
    * Try to guess the secret number within 10 seconds. The game will tell you if your guess is too high, too low, or correct.
    * After finishing the game, you'll be asked if you want to play again.
### Example Output
```bash
Choose a difficulty level:
1. Easy (1 to 10)
2. Hard (1 to 100)
Enter 1 for Easy or 2 for Hard: 1

Hello! I've picked a number between 1 and 10.
You have 3 attempts to guess the correct number.

Attempt 1:
Enter your guess: 4
Your guess is too low.

Attempt 2:
Enter your guess: 7
Your guess is too high.

Attempt 3:
Enter your guess: 6
Congratulations! You guessed the correct number on attempt 3!
Your final score: 1 points.

Do you want to play again? (yes/no): no
Thanks for playing!
```

## **Technical Detail**
* Python Version: The game was developed with Python 3.x.
* Libraries Used:
    * `random` for generating a random number.
    * `time` for measuring time and handling time limits.
    * `threading` to manage the timer asynchronously while accepting user input.

## **How To Contribute**
Feel free to contribute by submitting a pull request! Here are some ideas for how you can help:
    
* Improve the timer or scoring system.
* Add more levels of difficulty.
* Add sound effects or animations using a library like pygame.
* Enhance the user interface by integrating a GUI.
