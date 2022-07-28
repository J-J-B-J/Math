"""Find the range of a list of numbers"""
from Useful_Functions.get_list_numbers import get_list_numbers
from Useful_Functions.convert_to_int import convert_to_int


def find_range(numbers) -> float:
    """Find the range of a list of numbers"""
    return convert_to_int(max(numbers) - min(numbers))


def main(list_of_numbers: list = None) -> None:
    """Main function"""
    numbers = get_list_numbers(list_of_numbers=list_of_numbers)
    print("Range =", find_range(numbers))


if __name__ == "__main__":
    main()
