from stats import get_book_text
from stats import count_words

def main():
    book_text = get_book_text("books/frankenstein.txt")
    # print(book_text)
    num_words = count_words(book_text)

    print(f"{num_words} words found in the document")


main()