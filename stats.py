def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_count(char_counts):
    char_list = []
    for ch, count in char_counts.items():
        char_list.append({"char": ch, "num": count})

    char_list.sort(reverse=True, key=sort_on)
    return char_list
