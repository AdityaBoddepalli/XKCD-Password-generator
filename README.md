## XKCD password generator

One big reason why people choose weak passwords that are easily cracked is because they have been taught that only confusing passwords are secure. People either reject this advice and leave themselves vulnerable, or adopt password creation heuristics that are not resilient to cracking in practice (e.g., English word plus one capital letter, one random number, and one random symbol).

This is a python script that can generate secure, memorable passwords using the [XKCD method](https://xkcd.com/936/).

optional arguments:\
    -h, --help            show this help message and exit\
    -w WORDS, --words WORDS :- 
                          include WORDS words in the password (default=4)\
    -c CAPS, --caps CAPS :-  capitalize the first letter of CAPS random words
                          (default=0)\
    -n NUMBERS, --numbers NUMBERS :-
                          insert NUMBERS random numbers in the password
                          (default=0)\
    -s SYMBOLS, --symbols SYMBOLS :-
                          insert SYMBOLS random symbols in the password
                          (default=0)