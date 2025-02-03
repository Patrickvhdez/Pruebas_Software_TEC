"""
This module reads numerical data from a file, computes descriptive statistics
(mean, median, mode, variance, and standard deviation), and displays the results.
It also handles errors in the input data and writes the results to an output file.
"""

import sys
import time


def read_numbers_from_file(filename):
    """
    Reads numbers from a file and handles any invalid lines.

    Args:
        filename (str): The name of the file containing the data.

    Returns:
        tuple: A list of valid numbers and a list of error messages.
    """
    numbers = []
    errors = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                num = float(line.strip())
                numbers.append(num)
            except ValueError:
                errors.append(f"Invalid data at line {line_number}: '{line.strip()}'")
    return numbers, errors


def compute_mean(numbers):
    """
    Computes the mean of a list of numbers.

    Args:
        numbers (list): The list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    total_sum = 0
    for num in numbers:
        total_sum += num
    if len(numbers) == 0:
        return 0
    return total_sum / len(numbers)


def compute_median(numbers):
    """
    Computes the median of a list of numbers.

    Args:
        numbers (list): The list of numbers.

    Returns:
        float: The median of the numbers.
    """
    sorted_numbers = sorted(numbers)
    count = len(sorted_numbers)
    if count == 0:
        return 0
    if count % 2 == 1:
        return sorted_numbers[count // 2]
    return (sorted_numbers[count // 2 - 1] + sorted_numbers[count // 2]) / 2


def compute_mode(numbers):
    """
    Computes the mode(s) of a list of numbers. If no mode is found,
    returns a string indicating so.

    Args:
        numbers (list): The list of numbers.

    Returns:
        list or str: The mode(s) of the list or 'No mode' if there is none.
    """
    frequency_count = {}
    for num in numbers:
        if num in frequency_count:
            frequency_count[num] += 1
        else:
            frequency_count[num] = 1

    max_frequency = max(frequency_count.values(), default=0)
    modes = [key for key, value in frequency_count.items() if value == max_frequency]

    if len(modes) == len(numbers):
        return "No mode"
    return modes


def compute_variance(numbers, mean):
    """
    Computes the variance of a list of numbers.

    Args:
        numbers (list): The list of numbers.
        mean (float): The mean of the numbers.

    Returns:
        float: The variance of the numbers.
    """
    count = len(numbers)
    if count == 0:
        return 0
    variance_sum = 0
    for num in numbers:
        variance_sum += (num - mean) ** 2
    return variance_sum / count


def compute_standard_deviation(variance):
    """
    Computes the standard deviation of a list of numbers.

    Args:
        variance (float): The variance of the numbers.

    Returns:
        float: The standard deviation of the numbers.
    """
    return variance ** 0.5


def write_results_to_file(results, filename="StatisticsResults.txt"):
    """
    Writes the computed statistics to an output file.

    Args:
        results (list): A list of result strings to write to the file.
        filename (str): The name of the output file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for line in results:
            file.write(line + '\n')


def main():
    """
    Main entry point for the program. Reads a file of numbers,
    computes descriptive statistics, handles invalid data, and
    displays and saves the results.
    """
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py file_with_data.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    start_time = time.time()

    # Read numbers and handle invalid data
    numbers, errors = read_numbers_from_file(input_file)

    if len(errors) > 0:
        print("Errors encountered while reading the file:")
        for error in errors:
            print(error)

    # Compute statistics
    mean_value = compute_mean(numbers)
    median_value = compute_median(numbers)
    mode_value = compute_mode(numbers)
    variance_value = compute_variance(numbers, mean_value)
    standard_deviation_value = compute_standard_deviation(variance_value)

    # Prepare results for output
    results = [
        "Descriptive Statistics:",
        f"Mean: {mean_value}",
        f"Median: {median_value}",
        f"Mode: {mode_value if isinstance(mode_value, str) else ', '.join(map(str, mode_value))}",
        f"Variance: {variance_value}",
        f"Standard Deviation: {standard_deviation_value}",
        f"Total time elapsed: {time.time() - start_time:.4f} seconds"
    ]

    # Display results on the console
    for line in results:
        print(line)

    # Save results to a file
    write_results_to_file(results)


if __name__ == "__main__":
    main()
