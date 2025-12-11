  
def get_book_text(filepath):
    with open(filepath) as frankenstein:
        file_contents = frankenstein.read()
    return file_contents

from stats import word_count
from stats import character_count
from stats import sort_count
def main():
    text = get_book_text("books/frankenstein.txt")
    number_of_words = word_count(text)    
    print(f"Found {number_of_words} total words")
    char_counts = character_count(text)
    sorted_chars = sort_count(char_counts)
    print(sorted_chars)
main()


