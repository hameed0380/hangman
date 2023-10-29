import random

# function will take the guessed letter as an argument and check if the letter is in the word
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Iteratively check if the input is a valid guess
def ask_for_input():
    while True:
        guess = input("Please enter a letter: ")
        if guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    check_guess(guess)



word_list = ["apple", "banana", "orange", "pear", "pineapple"]
word = random.choice(word_list)

ask_for_input()