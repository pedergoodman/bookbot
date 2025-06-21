def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def count_words(book_text):
    word_list = []
    word_list = book_text.split()
    return len(word_list)