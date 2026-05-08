# Week 8
# Input Output files
# Rosie Navarro
# May 8, 2026


import os
import string

def word_count(word, word_count_dict):
    """
    Adds word to dictionary and increases count, if the word is there
    multiple times.

    Parameters:
        word (str): word being counted
        word_count_dict (dict): dictionary storing word frequency

    return: none
    """
    if word == "":
        return
    if word in word_count_dict:
        word_count_dict[word] += 1 # counts times words is seen
    else:
        word_count_dict[word] = 1


def process_line(line, word_count_dict):
    """
    purpose is to remove punctuation, split words.
        calls the add_word function at the end

    parameters:
        line (str): line read from input file
        word_count_dict (dict): dictionary storing word frequency

    return: none
    """

    split_words = line.split()
    for word in split_words:
        clean_words = word.translate(str.maketrans('', '', string.punctuation)).lower()
        # makes everything lowercase and removes spaces
        word_count(clean_words, word_count_dict)


def process_file(filename, word_count_dict):
    """
    Writes the word frequency table to output file

    parameters:
        filename (str): name of the output file the user want to use
        word_count_dict (dict): dictionary storing word frequency

    return: none
    """
    with open(filename, 'a') as fileHandle:
        fileHandle.write(f"{'Word': <20} {'count'}\n")
        fileHandle.write("-" * 25 + "\n")

    # words that are added to table
        for word, count in sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True):
            fileHandle.write(f"{word: <20} {count}\n")


def main():
    """
    Reads Gettysburg file, processes words, and writes the total
    number of unique words to a new file. Saves the results as a table.

    return: none
    """
    word_count_dict = dict()
    script_dir = os.path.dirname(os.path.abspath(__file__)) #folder where program is located
    file_path = os.path.join(script_dir, "gettysburg.txt") # input file being used
    filename = input("please entre file name you wish to use: ") # file name user wants (output name)

    try:
        with open(file_path, 'r') as file: # opens file to read
            for line in file:
                process_line(line, word_count_dict)
        with open(filename, 'w') as fileHandle: # opens file to write
            fileHandle.write(f"Total unique words: {len(word_count_dict)}\n")
        process_file(filename, word_count_dict)

    except FileNotFoundError: # error if file is not found
        print("File not Found")


main()
