ORDINALS = [
    'zeroth', 
    'first', 
    'second', 
    'third', 
    'fourth', 
    'fifth', 
    'sixth', 
    'seventh', 
    'eighth', 
    'ninth', 
    'tenth', 
    'eleventh', 
    'twelfth'
    ]
GIFTS = [
    '', #zeroth day
    'a Partridge in a Pear Tree.', 
    'two Turtle Doves, ', 
    'three French Hens, ', 
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
]

def recite(start_verse, end_verse):
    return [get_verse(day) for day in range(start_verse, end_verse + 1)]


def get_verse(verse):
    lines = [f'On the {ORDINALS[verse]} day of Christmas my true love gave to me: ']
    for i in range(verse, 0, -1):
        if i == 1 and verse > 1:
            lines.append('and ' + GIFTS[i])
        else:
            lines.append(GIFTS[i])
    
    return ''.join(lines)


