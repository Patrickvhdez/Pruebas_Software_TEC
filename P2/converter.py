"""Program to convert numbers from a file into their binary and hexadecimal representations.

The program reads a file provided as a command-line argument, processes the numbers,
converts them to binary and hexadecimal using basic algorithms, and outputs the results
to both the console and an output file. It also includes error handling for invalid data
and displays the total execution time.
"""
import sys
import time

# Function to convert a number to binary
def to_binary(number):
    """Convert an integer to its binary representation.

    Args:
        number (int): The number to convert.

    Returns:
        str: The binary representation of the number.
    """
    if number == 0:
        return "0"
    binary = ""
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary

# Function to convert a number to hexadecimal
def to_hexadecimal(number):
    """Convert an integer to its hexadecimal representation.

    Args:
        number (int): The number to convert.

    Returns:
        str: The hexadecimal representation of the number.
    """
    if number == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while number > 0:
        hexadecimal = hex_digits[number % 16] + hexadecimal
        number = number // 16
    return hexadecimal

# Main function
def main():
    """Main function to handle file input, process numbers, and manage output.

    Reads a file containing numbers, converts them to binary and hexadecimal,
    handles errors, and outputs the results to both the console and a file.
    """
    # Check if the program is invoked correctly
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        return

    input_file = sys.argv[1]
    output_file = "ConvertionResults.txt"

    try:
        # Read the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
        return

    start_time = time.time()
    results = []

    # Process each line in the input file
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line.isdigit():
            print(f"Warning: Invalid data on line {line_number}: '{line}'")
            continue

        number = int(line)
        binary_representation = to_binary(number)
        hexadecimal_representation = to_hexadecimal(number)

        result_line = f"Number: {number}, Binary: {binary_representation}, Hexadecimal: {hexadecimal_representation}"
        results.append(result_line)
        print(result_line)

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Write results to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + "\n")
        file.write(f"\nExecution Time: {elapsed_time:.2f} seconds\n")

    print(f"\nExecution Time: {elapsed_time:.2f} seconds")
    print(f"Results have been saved to '{output_file}'.")

if __name__ == "__main__":
    main()
