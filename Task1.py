import random

# Predefined list of 5 words
words = ["python", "computer", "program", "coding", "developer"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 6

# Display word with underscores
display_word = ["_"] * len(word)

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.\n")

while incorrect_guesses > 0 and "_" in display_word:

    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", incorrect_guesses)

    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check whether letter is in word
    if guess in word:
        print("Correct guess!\n")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        incorrect_guesses -= 1
        print("Wrong guess!\n")

# Final result
if "_" not in display_word:
    print("================================")
    print("Congratulations! You won!")
    print("The word was:", word)
    print("================================")
else:
    print("================================")
    print("Game Over!")
    print("The word was:", word)
    print("================================")

    

