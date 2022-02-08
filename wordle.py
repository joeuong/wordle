from datetime import date
import csv
from time import sleep

today = date.today()

date_word_dict= {}

with open('wordle_py.csv') as database:
    csvreader = csv.reader(database)
    for row in csvreader:
        date_word_dict[row[0]] = row[1]

today = today.strftime('%Y-%m-%d')
word_1 = date_word_dict[today]
word_1 = word_1.upper()
guess = 1

used_letters = []
letter_in_word = []

while guess < 6:
    print(f'Guess {guess} ---------------------------------------- ')

    word_1_index = 1
    word_1_letters_dict = {}
    for letter in word_1:
        word_1_letters_dict[word_1_index] = letter.upper()
        word_1_index += 1
        
    user_guess = input(f'Enter a word: ')
    user_guess = user_guess.upper()

    user_guess_index = 1
    user_guess_letters_dict = {}

    for letter in user_guess:
        user_guess_letters_dict[user_guess_index] = letter
        used_letters.append(letter)
        user_guess_index += 1
            
    if len(user_guess) != 5:
        print('Word needs to be 5 Letters')
        continue

    if user_guess == word_1:
        print(f'Congratulations, you guessed the word on Guess #{guess}')
        break
    
    else:
        a = 1
        while a < 6:
            if user_guess_letters_dict[a] == word_1_letters_dict[a]:
                print(f'Letter {user_guess_letters_dict[a]} is in the right spot')
                a += 1
                continue
            elif user_guess_letters_dict[a] in word_1_letters_dict.values():
                print(f'Letter {user_guess_letters_dict[a]} is in the word')
                del word_1_letters_dict[a]
                a += 1
                continue
            else:
                a += 1
                continue
    guess += 1
    sleep(2)

print('End of Game')
