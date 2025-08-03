def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = {}
    for char in text:
        lowercase_char = char.lower()
        char_count[lowercase_char] = char_count.get(lowercase_char, 0) + 1
    return char_count

def sort_char_counts_for_report(char_counts_dict):
    char_list_for_report = []
    for char, count in char_counts_dict.items():
        if char.isalpha(): # Check if the character is an alphabetical character
            char_list_for_report.append({"char": char, "num": count})

    # Sort the list of dictionaries from greatest to least by the 'num' (count)
    char_list_for_report.sort(key=lambda item: item["num"], reverse=True)
    return char_list_for_report
