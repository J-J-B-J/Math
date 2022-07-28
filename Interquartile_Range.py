"""Find the interquartile range of a list of numbers"""
from Useful_Functions.get_list_numbers import get_list_numbers
from Useful_Functions.convert_to_int import convert_to_int

from Median import find_median


def find_interquartile_range(numbers: list) -> float:
    """Find the interquartile range of a list of numbers"""
    numbers.sort()
    if len(numbers) % 2 == 0:
        lower_quartile = find_median(numbers[:len(numbers) // 2])
        upper_quartile = find_median(numbers[len(numbers) // 2:])
    else:
        lower_quartile = find_median(numbers[:len(numbers) // 2])
        upper_quartile = find_median(numbers[len(numbers) // 2 + 1:])
    return convert_to_int(upper_quartile - lower_quartile)


def main(list_of_numbers: list = None) -> None:
    """Main function"""
    numbers = get_list_numbers(list_of_numbers=list_of_numbers, sort=True)
    print("IQR =", find_interquartile_range(numbers))


if __name__ == "__main__":
    main()
