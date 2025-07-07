
#Recursive approach
def append(list1, list2):
    if list2 == []:
        return list1
    
    item, *tail = list2

    return append(list1 + [item], tail)


def concat(lists):
    if lists == []:
        return []
    
    item, *tail = lists

    return item + concat(tail)


def filter(function, list):
    if list == []:
        return []
    
    item, *tail = list
    
    if function(item):
        return [item] + filter(function, tail)

    return filter(function, tail)        


def length(list):
    if list == []:
        return 0
    
    _, *tail = list
    
    return 1 + length(tail)
    

def map(function, list, accumulator=[]):
    if length(list) == 0:
        return accumulator

    item, *tail = list
    return map(function, tail, accumulator + [function(item)])


def foldl(function, list, initial):
    if length(list) == 0:
        return initial
    
    item, *tail = list
    return foldl(function, tail, function(initial, item))


def foldr(function, list, initial):
    if length(list) == 0:
        return initial
    
    item, *tail = list
    return function(foldr(function, tail, initial), item)


def reverse(list):
    if length(list) == 0:
        return []
    
    item, *tail = list
    return reverse(tail) + [item]


'''
# Imperative approach

def append(list1, list2):
    return concat([list1, list2])

def concat(lists):
    #imperative approach
    total_length = sum(length(list) for list in lists)
    my_list = [None for _ in range(total_length)]

    starting_index = 0
    for list in lists:
        _add_elements(my_list, list, starting_index)
        starting_index += length(list)
    
    return my_list

def _add_elements(output_list, input_list, starting_index):
    for index, value in enumerate(input_list):
        output_list[index + starting_index] = value


def filter(function, list):
    my_list = []
    for element in list:
        if function(element):
            my_list = append(my_list, [element])
    
    return my_list

def length(list):
    return sum(1 for _ in list)    

    
def map(function, list):
    my_list = [None for _ in range(length(list))]
    for index, value in enumerate(list):
        my_list[index] = function(value)
    return my_list

def foldl(function, list, initial):
    accumulator = initial
    for value in list:
        accumulator = function(accumulator, value)
    
    return accumulator

def foldr(function, list, initial):
    return foldl(function, reverse(list), initial)

def reverse(list):
    for index in range(length(list)//2):
        list[index], list[-1 - index] = list[-1 - index], list[index]    
    return list
'''

