import re

def count_words(sentence):
    word_count = dict()
    words = re.split(r'[^A-Za-z0-9\']+', sentence.lower())

    for word in words:
        word = word.strip("'")
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count
