import csv
from collections import Counter, defaultdict as dd
from string import punctuation
import random


def csv_reader(filename):
    file = csv.DictReader(open(filename))
    return file


def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text


def bigrams_in_text(texts):
    all_bis = []
    for text in texts:
        for symbol in punctuation:
            text = text.replace(symbol, '')
        text = text.lower()
        words = text.split()
        bigrams = []
        for i in range(1, len(words)):
            bi = words[i - 1] + ' ' + words[i]
            bigrams.append(bi)
        bigrams = Counter(bigrams).most_common()
        all_bis.extend(bigrams)
    all_bis = [x[0] for x in all_bis]
    return all_bis


def dict_from_eps():
    files = ['SW_EpisodeIV.txt', 'SW_EpisodeV.txt', 'SW_EpisodeVI.txt']
    for filename in files:
        with open(filename, encoding='utf-8') as f:
            text = f.read()
        text = text.splitlines()[1:]
        remarks = dd(list)
        for line in text:
            number, char, text = line.split('" "', maxsplit=2)
            remarks[char.replace('"', '')].append(text.replace('"', ''))
    return remarks


def hints_from():
    csv = csv_reader('characters.csv')
    hints = {}
    for hint in csv:
        hints[hint['name']] = {
            'height': hint['height'],
            'mass': hint['mass'],
            'hair_color': hint['hair_color'],
            'skin_color': hint['skin_color'],
            'eye_color': hint['eye_color'],
            'birth_year': hint['birth_year'],
            'gender': hint['gender'],
            'homeworld': hint['homeworld'],
            'species': hint['species']

        }
    return hints


def mapping(char):
    hints = hints_from()
    for hint in hints:
        if char.lower() in [x.lower() for x in hint.split()]:
            answer = hints[hint]
            return answer


def game():
    remarks = dict_from_eps()
    char = random.choice(list(remarks))
    texts = remarks[char]
    hints = mapping(char)
    bis = bigrams_in_text(texts)
    print('Hello, I want to play a game with you.\n' \
          'Try to guess about what character from the SW Universe I think.\n')
    guess = ''
    tries = 0
    while guess.lower() != char.lower():
        if tries >= len(bis):
            print('I\'m sorry, I have no bigrams to show, you lost (in the woods)')
            break
        else:
            print('This character often says:', bis[tries])
            destiny = input('Would you like to try to guess (type "1"), get a hint (type "2") or give up'\
                            '(type "3")? ')
            if destiny == '1':
                guess = input('Who is it? ')
                tries += 1
            elif destiny == '2':
                if hints:
                    key = random.choice(list(hints))
                    value = hints[key]
                    print('Oh, I think you need a hint, here it is:')
                    print(f'{key} is {value}')
                    guess = input('Who is it? ')
                    tries += 1
                else:
                    print('There is no hints for this character')
                    guess = input('Who is it? ')
                    tries += 1
            else:
                print('You gave up!')
                break

    print('It was', char)
    print('Game over!')


if __name__ == '__main__':
    game()
