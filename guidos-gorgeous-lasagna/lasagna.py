"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
EXPECTED_PREP_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the expected prep time

    :param number_of_layers: int - number of layers in lasagna
    :return: int - expected prep time given the number of layers 

    Function that takes the number of layers of lasgna and calculates
    the expected prep time. EXPECTED_PREP_TIME is the number of minutes
    estimated to prep one layer of the lasagna.
    """

    return number_of_layers * EXPECTED_PREP_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calclate toal elapsed time

    :param number_of_layers: int - number of layers in lasagna
    :param elapsed_bake_time: int - minutes of time already in the oven
    :return: int - number of minutes spent prepping and cooking the lasagna so far
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
