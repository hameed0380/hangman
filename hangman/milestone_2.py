import random

word_list = ["apple", "banana", "orange", "pear", "pineapple"]
word = random.choice(word_list)

guess = input("Please enter a single letter: ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")


print(word_list)
print(word)