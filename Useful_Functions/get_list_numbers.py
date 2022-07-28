"""Get a list of numbers"""


def get_list_numbers(list_of_numbers: list, sort: bool = False) -> list:
    """Get a list of numbers"""
    if not list_of_numbers:
        list_of_numbers = input("Enter a list of numbers: ").split(", ")
        new_list = []
        for item in list_of_numbers:
            for item2 in item.split(" "):
                for item3 in item2.split(","):
                    new_list.append(float(item3))
        list_of_numbers = new_list
    if sort:
        list_of_numbers.sort()
    return list_of_numbers
