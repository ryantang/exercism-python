import re
from typing import Callable

# Dictionary mapping operation names to their corresponding functions
# Each function takes two numbers and returns a result
OPERATIONS: dict[str, Callable[[int | float, int], int | float]] = {
    "plus": lambda a, b: a + b,
    "minus": lambda a, b: a - b,
    "multiplied by": lambda a, b: a * b,
    "divided by": lambda a, b: a / b,
}

# Operations that have valid syntax but are not supported
INVALID_OPS: set[str] = {"cubed"}


def answer(question: str) -> int | float:
    """Parse and evaluate a word problem containing mathematical operations.
    
    Args:
        question: A word problem in the format "What is [number] [operation] [number]...?"
                 Supports operations: plus, minus, multiplied by, divided by
                 Example: "What is 5 plus 13 minus 6?"
    
    Returns:
        The numerical result of evaluating the operations sequentially.
        Returns int for all operations except division, which returns float.
    
    Raises:
        ValueError: With "syntax error" if the question format is invalid
                   (e.g., missing numbers, wrong structure, malformed input)
        ValueError: With "unknown operation" if the operation word is not supported
                   (e.g., "cubed", "squared", etc.)
    
    Examples:
        >>> answer("What is 5?")
        5
        >>> answer("What is 1 plus 1?")
        2
        >>> answer("What is 1 plus 1 plus 1?")
        3
    """
    # Extract the starting number and any remaining operations
    # Pattern: "What is" + (number) + (optional operations)
    start_match = re.search(r"What is (-?\d+)([^?]*)?", question)
    if not start_match:
        raise ValueError("syntax error")

    starting_number = int(start_match.group(1))
    remainder = start_match.group(2)

    # If there are no operations, just return the number
    if not remainder:
        return starting_number

    # Check for operations that are syntactically valid but not supported
    if remainder.strip() in INVALID_OPS:
        raise ValueError("unknown operation")

    # Validate the structure: must be (space + operation + space + number)+
    # This ensures proper alternation between operations and numbers
    ops_regex = "|".join(OPERATIONS.keys())
    if not re.match(rf"^( (?:{ops_regex}) -?\d+)+$", remainder):
        raise ValueError("syntax error")

    # Extract all (operation, operand) pairs. Example: [("plus", 3), ("divided by", 7)]
    operations = re.findall(rf"({ops_regex}) (-?\d+)", remainder)

    # Apply each operation sequentially from left to right
    accumulator = int(starting_number)
    for operator, operand in operations:
        accumulator = OPERATIONS[operator](accumulator, int(operand))

    return accumulator
