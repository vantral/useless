def read_file(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


def process_text(text, min_word_len=5, min_lemmas_count=2):
    items = re.findall('(\w+){([^}{]+)}', text)
    results = []
    for word, lemmas_raw in items:
        word = word.lower()
        lemmas = lemmas_raw.lower().replace('?', '').split('|')
        if len(word) >= min_word_len and len(lemmas) >= min_lemmas_count:
            results.append({'word': word, 'lemmas': lemmas})      
    return results


def solution(filename):
    text = read_file(filename)
    word_lemmas = process_text(text)
    
    def _lemmas_count(item):
        return len(item['lemmas'])
    
    word_lemmas.sort(key=_lemmas_count, reverse=True)
    
    with open('output.txt', 'w') as file:
        for word_lemmas in results:
            word = word_lemmas['word']
            lemmas = ','.join(word_lemmas['lemmas'])
            line = '{} -> {}\n'.format(word, lemmas)
            file.write(line)
