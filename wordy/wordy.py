import re

def answer(question):
    start_match = re.search(r"What is (-?\d+)([^?]*)?", question)
    if not start_match:
        raise ValueError("syntax error")

    starting_number = start_match.group(1)
    remaining_stuff = start_match.group(2)

    if starting_number and not remaining_stuff:
        return int(starting_number)

    if remaining_stuff.strip() in ("cubed"):
        raise ValueError("unknown operation")

    structure_pattern = r"^( (?:plus|minus|multiplied by|divided by) -?\d+)+$"
    if not re.match(structure_pattern, remaining_stuff):
        raise ValueError("syntax error")

    operations = re.findall(r"(plus|minus|multiplied by|divided by) (-?\d+)", remaining_stuff)
    print(f"operations is {operations}")

    accumulator = int(starting_number)
    for operation in operations:
        operator, operand = operation

        match operator:
            case "plus":
                accumulator = accumulator + int(operand)
            case "minus":
                accumulator = accumulator - int(operand)
            case "multiplied by":
                accumulator = accumulator * int(operand)
            case "divided by":
                accumulator = accumulator / int(operand)

    return accumulator
