def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    word_length = len(word)
    lowercased_word = word.lower()
    word_composition = letter_count(lowercased_word)

    anagrams = []
    for candidate in candidates:
        if lowercased_word == candidate.lower():
            continue # a word is not an anagram of itself
        if (word_length == len(candidate) and 
            word_composition == letter_count(candidate.lower())):
            anagrams.append(candidate)

    return anagrams

def letter_count(word: str) -> dict[str, int]:
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1

    return count