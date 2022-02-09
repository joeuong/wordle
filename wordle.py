from datetime import date
import csv
from time import sleep

today = date.today()

date_word_dict = {}

with open('wordle_py.csv') as database:
    csvreader = csv.reader(database)
    for row in csvreader:
        date_word_dict[row[0]] = row[1]

today = today.strftime('%Y-%m-%d')
word_1 = date_word_dict[today]
word_1 = word_1.upper()
guess = 0

used_letters = []
letter_in_word = []

while guess < 5:
    print(f'Guess {guess+1} ----------------------------')

    word_1_index = 0
    word_1_letters_dict = {}
    for letter in word_1:
        word_1_letters_dict[word_1_index] = letter.upper()
        word_1_index += 1
        
    user_guess = input(f'Enter a word: ')
    user_guess = user_guess.upper()

    user_guess_index = 0
    user_guess_letters_dict = {}

    for letter in user_guess:
        user_guess_letters_dict[user_guess_index] = letter
        used_letters.append(letter)
        user_guess_index += 1
            
    if len(user_guess) != 5:
        print('Word needs to be 5 Letters')
        continue

    if user_guess.lower() not in date_word_dict.values():
        print('Needs to be real 5-letter, non-plural word')
        continue
    
    if user_guess == word_1:
        print(f'Congratulations, you guessed the word on Guess #{guess+1}')
        break

    for k in user_guess_letters_dict:
    #todo - if there is a double-letter, display proper # of times
        if user_guess_letters_dict[k] in word_1_letters_dict.values():
            print(f'Letter {user_guess_letters_dict[k]} is in the word')

    for i in user_guess_letters_dict:
        if user_guess_letters_dict[i] == word_1_letters_dict[i]:
            print(f'Letter {user_guess_letters_dict[i]} is in the right spot')

    guess += 1

print(f'The word was {word_1}.')
print('End of Game')
