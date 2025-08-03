import sys
from stats import (get_num_words, 
                   character_count, 
                   sort_char_counts_for_report)




def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        print("Please ensure the provided path is correct and the file exists.")
        return ""


def main():
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]

    text = get_book_text(book_path)



    if text:
        num_words = get_num_words(text)
        char_counts_dict = character_count(text)
        sorted_char_data = sort_char_counts_for_report(char_counts_dict)


        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

            # Iterate through the sorted list and print each character and its count
        for item in sorted_char_data:
                print(f"{item['char']}: {item['num']}")

        print("============= END ===============")



main()