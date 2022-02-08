from english_words import english_words_lower_alpha_set
import random
from datetime import date, timedelta
import csv

today = date.today()

def get_five_letter_words(words):
    FLW = set()
    for word in words:
        if len(word) == 5:
            FLW.add(word)
    return FLW

words = get_five_letter_words(english_words_lower_alpha_set)

word_list = list(words)
word_list_len = len(word_list)

date_list = []

for i in range(word_list_len):
    date_list.append(today)
    today = today + timedelta(days=1)

result = zip(date_list,word_list)

for i in result:
    with open('wordle_py.csv', 'a', newline ='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(i)

