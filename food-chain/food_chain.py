VERSES = [
    "I don't know why she swallowed the fly. Perhaps she'll die.",
    "It wriggled and jiggled and tickled inside her.",
    "How absurd to swallow a bird!",
    "Imagine that, to swallow a cat!",
    "What a hog, to swallow a dog!",
    "Just opened her throat and swallowed a goat!",
    "I don't know how she swallowed a cow!",
    "She's dead, of course!",
]

ANIMALS = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse" ]
T_ANIMALS = ["fly", "spider that wriggled and jiggled and tickled inside her", "bird", "cat", "dog", "goat", "cow", "horse"]


def recite(start_verse, end_verse):
    if start_verse == 1:
        return [opening(0), VERSES[0]]
    if start_verse == 8:
        return [opening(7), VERSES[7]]


    start_idx = start_verse - 1
    verse = [opening(start_idx), VERSES[start_idx]]
    for i in range(start_idx -1, -1, -1):
        verse.append(transition(i))
    verse.append(VERSES[0])
    print(verse)
    return verse

def opening(verse_idx):
    return f"I know an old lady who swallowed a {ANIMALS[verse_idx]}."

def transition(verse_idx):
    return f"She swallowed the {ANIMALS[verse_idx+1]} to catch the {T_ANIMALS[verse_idx]}."
