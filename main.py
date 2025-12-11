import sys
from stats import word_count, character_count, sort_count

def get_book_text(filepath):
    with open(filepath) as frankenstein:
        file_contents = frankenstein.read()
    return file_contents
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]  # current default book
    text = get_book_text(filepath)

    number_of_words = word_count(text)
    char_counts = character_count(text)
    sorted_chars = sort_count(char_counts)

    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()