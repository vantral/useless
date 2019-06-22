##Buzanov Anton

import re, os, random, pprint, time, collections

def open_file(filename):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    return text

def clear(text):
    pattern = '<w><.+>(.+?)</w>'
    words = re.findall(pattern, text)
    words = map(lambda x: x.lower(), words)
    return words

def freq():
    files = os.listdir('.') ##files should be placed in the current folder
    all_words = []
    len_text = 0
    for file in files:
        if file.endswith('union'):
            a = open_file(file)
            b = clear(a)
            all_words.extend(b)
    counter = collections.Counter(all_words)
    for key in counter:
        counter[key] = counter[key] / len(all_words)
    return counter

def task1(counter):
    lines = []
    for key in reversed(sorted(counter, key=counter.get)):
        line = key + '\t' + str(counter[key])
        lines.append(line)
    fin = '\n'.join(lines)
    with open('freq.tsv', 'w', encoding='utf-8') as f:
            f.write(fin)


def split(text):
    pattern = '<html path="(.+)"><body>'
    names = re.findall(pattern, text)
    pattern = '<html path=".+"><body>'
    texts = re.split(pattern, text)
    texts = texts[1:]
    new_texts = []
    for text in texts:
        n = texts.index(text)
        text = '<html path="' + names[n] + '"><body>' + text
        new_texts.append(text)
    folders = map(lambda x: './' + os.path.dirname(x), names)
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
    for name in names:
        num = names.index(name)
        with open(name, 'w', encoding='utf-8') as f:
            f.write(new_texts[num])

def task2():
    files = os.listdir('.')
    for file in files:
        if file.endswith('union'):
            split(open_file(file))

def find_lemmas(text):
    pattern = '<html path="(.+)\.mystem"><body>'
    path = re.search(pattern, text).groups(1)[0]
    pattern = '<w><ana lex="(.+?)"'
    lemmas = re.findall(pattern, text)
    path += '.lemma' 
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lemmas))

def task3():
    for root, _, files in os.walk('.'):
        for file in files:
            if file.endswith('mystem'):
                path = os.path.join(root, file)
                find_lemmas(open_file(path))

    
def main():
    task1(freq()) #####THIS IS THE FIRST TASK
    task2() ####THIS IS THE SECOND TASK
    task3() ####THIS IS THE THIRD TASK
    

if __name__ == '__main__':
    main()
