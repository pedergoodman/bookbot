from stats import get_book_text
from stats import count_words
from stats import count_characters
from stats import sort_dictionary
from stats import create_report
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)

    num_words = count_words(book_text)
    print(f"{num_words} words found in {path_to_book}")

    # count_characters(book_text)
    # sort_dictionary(count_characters(book_text))
 
    create_report(book_text)

main()