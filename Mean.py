"""Find the mean of a list of numbers"""
from Useful_Functions.get_list_numbers import get_list_numbers
from Useful_Functions.convert_to_int import convert_to_int


def find_mean(numbers: list) -> float:
    """Find the mean of a list of numbers"""
    total = 0
    for i in numbers:
        total += i
    return convert_to_int(total / len(numbers))


def main(list_of_numbers: list = None) -> None:
    """Main function"""
    numbers = get_list_numbers(list_of_numbers=list_of_numbers)
    print("Mean =", find_mean(numbers))


if __name__ == "__main__":
    main()
