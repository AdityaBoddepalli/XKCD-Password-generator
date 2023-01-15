#!/usr/bin/env python3

import argparse
import random

argparse = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
argparse.add_argument('-w', '--words', default=4, type=int, help='include this many words in the password')
argparse.add_argument('-c', '--caps', default=0, type=int, help='capitalize the first letter of this many random words')
argparse.add_argument('-n', '--numbers', default=0, type=int, help='insert this many random numbers in the password')
argparse.add_argument('-s', '--symbols', default=0, type=int, help='insert this many random symbols in the password')
args = argparse.parse_args()

def random_word_getter(num):
    list_of_words = []
    for i in range(num):
        word = random.choice(open("words.txt").readlines())
        size = len(word)
        word = word[:size - 1]
        list_of_words.append(word)
    return list_of_words

def capitalise(word):
    return word.capitalize()


def add_nums(word):

    frontorback = [1, 0]
    i = random.choice(frontorback)
    num_list = ["0","1","2","3","4","5","6","7","8","9"]
    if i == 1:
        return random.choice(num_list) + word
    else:
        return word + random.choice(num_list)


def add_symbols(word):

    frontorback = [1, 0]
    i = random.choice(frontorback)
    sym_list = ["~","!","@", "#", "$", "%", "^", "&", "*", ".", ":", ";"]
    if i == 1:
        return random.choice(sym_list) + word
    else:
        return word + random.choice(sym_list)


def password_gen(no_of_words, no_of_caps, no_of_nums, no_of_symbols):
    words = random_word_getter(no_of_words)
    indexes = list(range(len(words)))
    if no_of_caps > no_of_words:
        no_of_caps = no_of_words
    for i in range(no_of_caps):
        indexX = random.choice(indexes)
        word_to_be_cap = words[indexX]
        indexes.remove(words.index(word_to_be_cap))
        words[indexX] = capitalise(word_to_be_cap)
    for i in range(no_of_nums):
        word_to_be_num = random.choice(words)
        indexX = words.index(word_to_be_num)
        words[indexX] = add_nums(word_to_be_num)
    for i in range(no_of_symbols):
        word_to_be_sym = random.choice(words)
        indexX = words.index(word_to_be_sym)
        words[indexX] = add_symbols(word_to_be_sym)
    return ''.join(words)

print(password_gen(args.words, args.caps, args.numbers, args.symbols))