def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()


def count_words(book_text):
    word_list = []
    word_list = book_text.split()
    return len(word_list)

def count_characters(book_text):
    lower_case_text = book_text.lower()
    char_dict = {}

    for char in lower_case_text:
        if char in char_dict:
            char_dict[char] += 1
        else: 
            char_dict.update({char: 1})

    print(char_dict)