from collections.abc import Iterable

def flatten(iterable):
    flattened_list = []
    for obj in iterable:
        if isinstance(obj, Iterable):
            values = flatten(obj)
            flattened_list += values
        elif obj is None:
            continue
        else:
            flattened_list += [obj]

    return flattened_list

    
