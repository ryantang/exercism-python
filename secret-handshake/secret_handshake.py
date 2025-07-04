ACTION_LIST = ['wink', 'double blink', 'close your eyes', 'jump']

def commands(binary_str: str) -> list[str]:
    """ Decode a binary string into a list of secret actions.

    Args:
        binary_str: str - a binary number that codes into actions
    
    Returns:
        List[str]: list of actions based on the binary_str input
    
    Example:
       >>> commands('00011')
       ['wink', 'double blink']    
    """
    reverse, *action_codes = binary_str

    actions = []
    for index, code in enumerate(action_codes[::-1]):
        if code == '1':
            actions.append(ACTION_LIST[index])

    if reverse == '1':
        return actions[::-1] 

    return actions
