def transform(legacy_data):
    new_scoring = {}
    for point_value, letters in legacy_data.items():
        for letter in letters:
            new_scoring[letter.lower()] = point_value

    return new_scoring


'''
#recursive approach
def transform(legacy_data, accumulator = None):
    if accumulator is None:
        accumulator = {}

    if legacy_data == {}:
        return accumulator
    
    my_data = legacy_data.copy()
    point_value, letters = my_data.popitem()

    accumulator = _create_point_dict(point_value, letters, accumulator)

    return transform(my_data, accumulator)


def _create_point_dict(point_value, letters, accumulator):
    if letters == []:
        return accumulator
    
    letter, *tail = letters
    accumulator[letter.lower()] = point_value

    return _create_point_dict(point_value, tail, accumulator)
'''