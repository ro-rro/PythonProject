# Week 8
# Rosie Navarro
# May 8, 2026



import os
import string

def word_count(word, word_count_dict):
    if word == "":
        return
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def process_line(line, word_count_dict):
    split_words = line.split()
    for word in split_words:
        clean_words = word.translate(str.maketrans('', '', string.punctuation)).lower()
        word_count(clean_words, word_count_dict)


def process_file(filename, word_count_dict):
    with open(filename, 'a') as fileHandle:
        fileHandle.write(f"{'Word': <20} {'count'}\n")
        fileHandle.write("-" * 25 + "\n")

    # words that are added to table
        for word, count in sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True):
            fileHandle.write(f"{word: <20} {count}\n")


def main():
    word_count_dict = dict()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "gettysburg.txt")
    filename = input("please entre file name you wish to use: ")

    try:
        with open(file_path, 'r') as file:
            for line in file:
                process_line(line, word_count_dict)
        with open(filename, 'w') as fileHandle:
            fileHandle.write(f"Total unique words: {len(word_count_dict)}\n")
        process_file(filename, word_count_dict)

    except FileNotFoundError:
        print("File not Found")

main()
