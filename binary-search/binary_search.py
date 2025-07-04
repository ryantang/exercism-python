def find(search_list, value):
    length = len(search_list)

    if length == 0:
        raise ValueError("value not in array")        

    midpoint_index = length//2
    midpoint_value = search_list[midpoint_index]

    if value == midpoint_value:
        return midpoint_index
    elif value < midpoint_value:
        return find(search_list[:midpoint_index], value)
    elif value > midpoint_value:
        return midpoint_index + 1 + find(search_list[midpoint_index + 1:], value)
    



