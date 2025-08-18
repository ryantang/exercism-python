import string

def score(word):
    points = points_mapping()

    return sum(
        points[letter.lower()]
        for letter in word
    )

def points_mapping():
    points_to_letters = {
        1: 'aeioulnrst',
        2: 'dg',
        3: 'bcmp',
        4: 'fhvwy',
        5: 'k',
        8: 'jx',
        10: 'qz'
    }

    return {
        letter: points
        for (points, letters) in points_to_letters.items()
        for letter in letters
    }




