"""Convert a float to an int if they are equal"""


def convert_to_int(number: float):
    """Convert a float to an int if they are equal"""
    if int(number) == number:
        return int(number)
    else:
        return number
