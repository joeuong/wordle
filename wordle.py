from datetime import date
from collections import Counter
import csv

today = date.today()

date_word_dict = {}

with open('wordle_py.csv') as database:
    csvreader = csv.reader(database)
    for row in csvreader:
        date_word_dict[row[0]] = row[1]

today = today.strftime('%Y-%m-%d')
word = date_word_dict[today]
word = word.upper()
guess = 0

used_letters = []
letter_in_word = []

l = '_'
m = '_'
n = '_'
o = '_'
p = '_'

while guess < 5:
    print(f'Guess {guess+1} ----------------------------')
    print('Enter "1" for Used Letters; Enter "2" for Correct Letters')

    word_index = 0
    word_letters_dict = {}
    for letter in word:
        word_letters_dict[word_index] = letter.upper()
        word_index += 1
        
    user_guess = input(f'Enter a word: ')
    user_guess = user_guess.upper()

    user_guess_index = 0
    user_guess_letters_dict = {}

    for letter in user_guess:
        user_guess_letters_dict[user_guess_index] = letter
        used_letters.append(letter)
        user_guess_index += 1

    if user_guess == '1':
        res = []
        [res.append(x) for x in used_letters if x not in res]
        alpha_res = list([val for val in res if val.isalpha()])
        alpha_res.sort()
        print(alpha_res)
        continue

    if user_guess == '2':
        print(l,m,n,o,p)
        continue

    if len(user_guess) != 5:
        print('Word needs to be 5 Letters')
        continue

    if user_guess.lower() not in date_word_dict.values():
        print('Needs to be real 5-letter, non-plural word')
        continue
    
    if user_guess == word:
        print(f'Congratulations, you guessed the word on Guess #{guess+1}')
        break

    a = user_guess_letters_dict[0]
    b = user_guess_letters_dict[1]
    c = user_guess_letters_dict[2]
    d = user_guess_letters_dict[3]
    e = user_guess_letters_dict[4]

    word_letters_list = list(word_letters_dict.values())

    if a == word_letters_dict[0]:
        a = user_guess_letters_dict[0]
        l = user_guess_letters_dict[0]
    elif a in word_letters_list:
        word_letters_list.remove(a)
        a = user_guess_letters_dict[0].lower()
    elif a not in word_letters_list:
        a = '_'

    if b == word_letters_dict[1]:
        b = user_guess_letters_dict[1]
        m = user_guess_letters_dict[1]
    elif b in word_letters_list:
        word_letters_list.remove(b)
        b = user_guess_letters_dict[1].lower()
    elif b not in word_letters_list:
        b = '_'

    if c == word_letters_dict[2]:
        c = user_guess_letters_dict[2]
        n = user_guess_letters_dict[2]
    elif c in word_letters_list:
        word_letters_list.remove(c)
        c = user_guess_letters_dict[2].lower()
    elif c not in word_letters_list:
        c = '_'

    if d == word_letters_dict[3]:
        d = user_guess_letters_dict[3]
        o = user_guess_letters_dict[3]
    elif d in word_letters_list:
        word_letters_list.remove(d)
        d = user_guess_letters_dict[3].lower()
    elif d not in word_letters_list:
        d = '_'

    if e == word_letters_dict[4]:
        e = user_guess_letters_dict[4]
        p = user_guess_letters_dict[4]
    elif e in word_letters_list:
        word_letters_list.remove(e)
        e = user_guess_letters_dict[4].lower()
    elif e not in word_letters_list:
        e = '_'
    
    print(a,b,c,d,e)
    guess += 1

print('---------------------------------------')
print(f'The word was {word}.')
print('End of Game')
