def response(hey_bob):
    if _is_silence(hey_bob):
        return "Fine. Be that way!"
    if _is_yelling(hey_bob) and _is_question(hey_bob):
        return "Calm down, I know what I'm doing!"
    if _is_question(hey_bob):
        return "Sure."
    if _is_yelling(hey_bob):
        return "Whoa, chill out!"
    else:
        return "Whatever."
    

def _is_question(hey_bob):
    return hey_bob.strip().endswith("?")

def _is_yelling(hey_bob):
    letters = [char for char in hey_bob if char.isalpha()]

    if not letters: #short-circuit if no letters found
        return False
    
    return all(char.isupper() for char in letters)

def _is_silence(hey_bob):
    return not hey_bob.strip() 