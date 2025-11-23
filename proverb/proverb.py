def proverb(*data, qualifier=None):
    if not data:
        return []
    
    text = []
    for i in range(len(data) - 1):
        text.append(f"For want of a {data[i]} the {data[i+1]} was lost.")

    if qualifier is None:
        text.append(f"And all for the want of a {data[0]}.")
    else:
        text.append(f"And all for the want of a {qualifier} {data[0]}.")

    return text

    
