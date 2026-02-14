import re

def answer(question):
    start_match = re.search(r"What is (-?\d+)", question)
    starting_number = start_match.group(1)
    print(f'starting number is {starting_number}')

    operations = re.findall(r"(plus|minus|multiplied by|divided by) (-?\d+)", question)
    print(f"operations is {operations}")

    if starting_number and not operations:
        return int(starting_number)

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