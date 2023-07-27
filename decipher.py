"""Decipher ciphered texts from ConnieLingus' CaitVi Noir!
"""


import re


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open('dictionary.txt') as f:
    DICTIONARY = set(f.read().upper().split())

WORD_PATTERN = re.compile(r'[A-Z]+')


def letter_to_number(letter):

    if letter.upper() in ALPHABET:
        return ALPHABET.index(letter.upper())
    else:
        return letter


def shift_number(number, shift):

    if isinstance(number, int):
        return (number - shift) % 26
    else:
        return number


def number_to_letter(number):

    if isinstance(number, int):
        return ALPHABET[number]
    else:
        return number


def shift_text(text, shift):

    numbers = [letter_to_number(x) for x in text]
    numbers = [shift_number(x, shift) for x in numbers]
    letters = [number_to_letter(x) for x in numbers]
    return ''.join(letters)


def word_score(text):

    words = WORD_PATTERN.findall(text.upper())
    return sum([word in DICTIONARY for word in words])


def decipher_text(text):

    best_score = 0
    best_texts = []

    for i in range(26):

        shifted_text = shift_text(text, i)
        score = word_score(shifted_text)

        if score > best_score:
            best_score = score
            best_texts = [(shifted_text, i)]
        elif score == best_score:
            best_texts.append((shifted_text, i))

    return best_texts


if __name__ == '__main__':

    text = input('text: ')
    deciphered_texts = decipher_text(text)

    for text, shift in deciphered_texts:
        print(f'\n#### {shift} ####\n{text}\n###########')
