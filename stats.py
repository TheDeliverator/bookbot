def sort_on(items):
    return items["num"]

def get_num_words(book_text):
    text_list = book_text.split()
    return(len(text_list))

def get_char_count(book_text):
    char_list = list()
    char_dict = dict()

    for char in list(book_text):
        if char.isalpha():
            char=char.lower()
            char_dict[char] = char_dict.get(char, 0) + 1

    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    
    char_list.sort(key=sort_on, reverse=True)
    return char_list