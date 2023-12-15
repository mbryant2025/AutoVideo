# Generates videos along the lines of "Only true Swifties know which Taylor Swift songs have the word 'love' in the title"
# Or "Only true Swifties know which Taylor Swift songs have the word 'horse' in them

import csv
import random
from src.swift_words import find_titles

# CSV header is Word,Frequency
word_list_file = 'data/title_word_frequency.csv'


# Choose a word that is in at least 2 and at most 5 songs
def choose_word():
    with open(word_list_file, 'r') as f:
        reader = csv.reader(f)
        word_list = list(reader)

    # Remove header
    word_list = word_list[1:]

    # Remove words that are in more than 5 songs
    word_list = [word for word in word_list if 2 <= int(word[1]) <= 5]


    # Choose a random word
    return random.choice(word_list)[0]

# Get all the titles that have the word in them
def get_titles(word):
    return find_titles(word)

word = choose_word()
titles = get_titles(word)

print(f"Only true Swifties know which {len(titles)} Taylor Swift songs have the word '{word}' in the title")
input()
print(get_titles(word))
