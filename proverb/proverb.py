def proverb(*data, qualifier):

    if len(data) == 0:
        return []
    
    text = []
    first_item = ""
    previous = ""
    for i, item in enumerate(data):
        if i == 0:
            first_item = item
            previous = item
        else:
            line = f"For want of a {previous} the {item} was lost."
            text.append(line)
            previous = item
    
    if qualifier == None:
        text.append(f"And all for the want of a {first_item}.")
    else:
        text.append(f"And all for the want of a {qualifier} {first_item}.")

    return text

    
