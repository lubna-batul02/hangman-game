import random

def hangman():
    words = ["python", "java", "ruby", "swift", "html"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("_ " * len(secret_word))

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in secret_word:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess!")
            guessed_letters.append(guess)
            incorrect_guesses += 1
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

    if incorrect_guesses == max_incorrect_guesses:
        print("You ran out of guesses! The word was:", secret_word)

if __name__ == "__main__":
    hangman()
