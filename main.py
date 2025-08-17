import sys
from stats import get_num_words
from stats import get_char_count

def get_book_text(book_file):
    with open(book_file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    book_text = get_book_text(book_file)
    num_words = get_num_words(book_text)
    char_list = get_char_count(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
main()