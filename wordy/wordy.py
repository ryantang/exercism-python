import re

def answer(question):
    pattern = r"What is (-?\d+)( \w+\s?\w* )?(-?\d+)?\?"
    result = re.search(pattern, question)

    if result:

        operator = result.group(2)
        if isinstance(operator, str):
            operator = operator.strip()
            print(f'operator is {operator}')

        match operator:
            case None:
                return int(result.group(1))
            case "plus":
                return int(result.group(1)) + int(result.group(3))
            case "minus":
                return int(result.group(1)) - int(result.group(3))
            case "multiplied by":
                return int(result.group(1)) * int(result.group(3))
            case "divided by":
                return int(result.group(1)) / int(result.group(3))

