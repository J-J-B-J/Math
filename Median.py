"""Find the median of a list of numbers"""
from Useful_Functions.get_list_numbers import get_list_numbers
from Useful_Functions.convert_to_int import convert_to_int


def find_median(numbers: list) -> float:
    """Find the median of a list of numbers"""
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        median = numbers[len(numbers) // 2]
    return convert_to_int(median)


def main(list_of_numbers: list = None) -> None:
    """Main function"""
    numbers = get_list_numbers(list_of_numbers=list_of_numbers, sort=True)
    print("Median =", find_median(numbers))


if __name__ == "__main__":
    main()
