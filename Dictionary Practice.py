# 7.1 Programming Assignment
# Rosie Navarro
# 04/30/26


import os
import string

def add_word(word, word_count_dict):
    """
    Parameters: word, and word_count_dict
    Purpose adds each words to the dictionary
    """
    #if there is a space it is removed used the code below
    if word == "":
        return
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def process_line(line, word_count_dict):
    """
    parameters: line and word_count_dict

    purpose is to remove punctuation, split words.
        calls the add_word function at the end
    """

    split_words = line.split()
    for word in split_words:
        clean_word = word.translate(str.maketrans('', '', string.punctuation)).lower()
        add_word(clean_word, word_count_dict)

def pretty_print(word_count_dict):
    """
    parameter: word_count_dict
    Prints the word frequency in a table sorted from highest to lowest.
    """

    # below is the actual table but without the numbers
    print (f"\n{'Word': <20} {'Count'}")
    print("-" * 30)

    # words that are added to table
    for word, count in sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{word: <20} {count}")


def main():
    """
    Reads the Gettysburg text, and processes each line to build a table.
    Prints the total number of unique words can counts the times they appear.
    """

    word_count_dict = {}
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "gettysburg.txt")

    try:
        with open(file_path, 'r') as file:
            for line in file:
                process_line(line, word_count_dict)
    except FileNotFoundError:
        print("Error")


    print(len(word_count_dict))
    pretty_print(word_count_dict)

# calls main function
main()
