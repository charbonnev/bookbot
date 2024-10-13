from typing import Counter

def sort_on(dict):
    return dict["count"]

def count_words(book_as_string):
    return len(book_as_string.split())

def count_each_character(book_as_string):
    char_dict = Counter(book_as_string.lower())
    # book_as_string = book_as_string.lower()
    # for char in book_as_string: #modo menos eficiente
    #     if char in char_dict:
    #         char_dict[char]+=1
    #     else:
    #         char_dict[char]=1
    return char_dict

def dict_to_sorted_list_of_dicts(the_dict):
    result = [{'character':char, 'count':count} for char,count in the_dict.items() if char.isalpha()]
    result.sort(reverse=True, key=sort_on)
    return result

def main():
    full_filepath = 'books/frankenstein.txt'
    with open(full_filepath) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_each_character(file_contents)
    char_count = dict_to_sorted_list_of_dicts(char_count)
    
    print(f"--- Begin report of {full_filepath} ---")
    print(f"${word_count} words found in the document")
    print("")
    for item in char_count:
        print(f"The '{item['character']}' character was found {item['count']} times")
    
    
main() 