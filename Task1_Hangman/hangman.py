
import random

# List of secret words
words = ["python", "computer", "program", "developer", "keyboard"]

# ASCII hangman stages
hangman_art = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

# Select a random word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
wrong_attempts = 0
max_attempts = 6

print("===== HANGMAN GAME =====")

# Main game loop
while wrong_attempts < max_attempts:

    print(hangman_art[wrong_attempts])

    # Display guessed word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter.upper() + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print("Attempts left:", max_attempts - wrong_attempts)
    print("Guessed letters:", guessed_letters)

    # Check victory
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    guess = input("\nGuess a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Prevent duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_attempts += 1
        print("Wrong guess!")

else:
    print(hangman_art[wrong_attempts])
    print("\nGame Over! You lost.")
    print("The secret word was:", secret_word)

print("\nThank you for playing Hangman!")