"""
This program reads a text file, counts the frequency of distinct words,
prints the results to the console, and writes them to an output file.
"""

import sys
import time

# Function to count word frequencies using basic algorithms
def count_words(content):
    """Counts the frequency of each distinct word in the provided content."""
    word_frequency = {}
    current_word = ""

    for char in content:
        # Check for word separators (spaces, newlines, punctuation)
        if char.isalnum():
            current_word += char.lower()
        else:
            if current_word:  # If word is non-empty, process it
                if current_word in word_frequency:
                    word_frequency[current_word] += 1
                else:
                    word_frequency[current_word] = 1
                current_word = ""

    # For the last word if the file doesn't end with a space or newline
    if current_word:
        if current_word in word_frequency:
            word_frequency[current_word] += 1
        else:
            word_frequency[current_word] = 1

    return word_frequency

# Main program
if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    INPUT_FILE = sys.argv[1]

    try:
        start_time = time.time()

        # Read the file content
        with open(INPUT_FILE, 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Count the word frequencies
        word_frequencies = count_words(file_content)

        # Prepare output
        output_lines = ["Word Frequency Results:\n"]
        for word, count in sorted(word_frequencies.items()):
            output_lines.append(f"{word}: {count}\n")

        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        output_lines.append(f"\nTime elapsed: {elapsed_time:.2f} seconds\n")

        # Print results to console
        for line in output_lines:
            print(line, end="")

        # Write results to WordCountResults.txt
        with open("WordCountResults.txt", 'w', encoding='utf-8') as result_file:
            result_file.writelines(output_lines)

    except FileNotFoundError:
        print(f"Error: File '{INPUT_FILE}' not found.")
    except OSError as e:
        print(f"An error occurred while processing the file: {e}")
