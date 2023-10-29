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
            for i, word_letter in enumerate(self.word):
                if word_letter == guess:
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
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter: {guess}")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

def play_game(word_list):

    game = Hangman(word_list, num_lives=5)
    print(f"The mystery word has {game.num_letters} characters")
    print(f"{game.word_guessed}")
    
    while True:
        if game.num_lives == 0:
            print(f'You lost! The word was "{game.word}"')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break




    
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)