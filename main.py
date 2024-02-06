def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    letter_count = get_letter_count(text)

    print_book_report(num_words, letter_count)


    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    words_list = text.split()
    return len(words_list)

def get_letter_count(text):
    letter_count_dict = {}

    for char in text.lower():
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1
    return letter_count_dict

def sort_on(dict):
    return dict["freq"]

def dict_to_sorted_list(letter_count):
    char_lst = []

    for char in letter_count:
        if char.isalpha():
            char_lst.append({"char": char, "freq": letter_count[char]})

    char_lst.sort(reverse=True, key=sort_on)
    return char_lst

def print_book_report(num_words, letter_count):

    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    print("Listing character counts by frequency:")

    sorted = dict_to_sorted_list(letter_count)

    for dict in sorted:
        char = dict["char"]
        freq = dict["freq"]
        print(f"The '{char}' character was found {freq} times")

    print("--- End report ---")
    

main()
    
