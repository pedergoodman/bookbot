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

    # print(char_dict)
    return char_dict

def sort_on(items):
    return items["num"]


# accepts dictionary, returns sorted dict list
def sort_dictionary(dict):
    new_list = []
    for key, value in dict.items():
        # print(f"{key} : {value}")
        # pass on special characters
        if key.isalpha():
        # create a k:v pair
            new_dict = {"char": key, "num": value}
        # add it to the list
            new_list.append(new_dict)

    #sort list
    new_list.sort(reverse=True, key=sort_on)
    # print(new_list)
    return new_list


# 
def create_report(book_text):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")

    sorted_chars = sort_dictionary(count_characters(book_text))
    
    for item in sorted_chars:
        char = item['char']
        num = item['num']
        print(f"{char}: {num}")