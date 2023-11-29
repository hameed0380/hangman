import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
        function will take the guessed letter as an argument and check if the letter is in the word
        '''
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

    def ask_for_input(self):
        '''
        Iteratively check if the input is a valid guess
        '''
        while True:
            guess = input("Please enter a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter: {guess}")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.word_guessed)
                break

def play_game(word_list):
    '''
    Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    If the user guesses the word, print "Congratulations! You won!"
    If the user runs out of lives, print "You lost! The word was {word}"
    '''
    game = Hangman(word_list, num_lives=5)
    print(f"The mystery word has {len(game.word)} characters")
    print(f"{game.word_guessed}")
    
    while True:
        if game.num_lives == 0:
            print(f'You lost! The word was "{game.word}"')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            print(f"The word is: {game.word_guessed}")
            break

    
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)