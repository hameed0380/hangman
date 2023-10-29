import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    # function will take the guessed letter as an argument and check if the letter is in the word
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
                    self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    # Iteratively check if the input is a valid guess
    def ask_for_input(self):
        while True:
            guess = input("Please enter a letter: ").lower()
            if not guess.isalpha() and len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                "You already tried that letter!"
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

    

word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
hangman_game = Hangman(word_list)
hangman_game.ask_for_input()