import re
import collections
import json


def read_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def get_bigrams(text):
    words = re.findall('(\w+)', text.lower())
    bigrams = []
    for i in range(0, len(words) - 1):
        bigrams.append((words[i], words[i + 1]))
    return bigrams


def create_bigrams_counter(utterances):
    counter = collections.Counter()
    for utterance in utterances:
        counter.update(get_bigrams(utterance))
    return counter


def get_utterances(data):
    result = []
    for dialogue in data:
        for turn in dialogue['turns']:
            if turn['speaker'] == 'USER':
                result.append(turn['utterance'])
    return result


def solution(filename):
    data = read_json(filename)
    utterances = get_utterances(data)
    counter = create_bigrams_counter(utterances)

    with open('output.txt', 'w') as file:
        for (left, right), freq in counter.most_common(None):
            line = '({}, {}) -> {}\n'.format(left, right, freq)
            file.write(line)
