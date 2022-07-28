"""Find the mode of a list of numbers."""
from Useful_Functions.get_list_numbers import get_list_numbers
from Useful_Functions.convert_to_int import convert_to_int


def find_mode(numbers: list) -> float:
    """Find the mode of a list of numbers."""
    if len(numbers) == 1:
        return numbers[0]
    counts = {}
    for num in numbers:
        if num in counts.keys():
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    return convert_to_int([num for num, count in counts.items() if count ==
                           max_count][0])


def main(list_of_numbers: list = None) -> None:
    """Main function"""
    numbers = get_list_numbers(list_of_numbers=list_of_numbers)
    print("Mode =", find_mode(numbers))


if __name__ == "__main__":
    main()
