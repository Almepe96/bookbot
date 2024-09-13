def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = word_count(text)
    each_letter = letter_count(text)            #list of dictionaries
    sorted_letters = sort_letters(each_letter)
    word_report(path, num_words, sorted_letters)

def sort_on(letter_dict):
    return letter_dict["num"]

def sort_letters(dict):
    sorted_list = []
    for k in dict:
        sorted_list.append({"char":k, "num":dict[k]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def word_report(path, num_words, each_letter):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for letter_dict in each_letter:
        print(f"The {letter_dict['char']} character was found {letter_dict['num']} times")
    print("--- End report ---")

def letter_count(text):
    letter_count = {}
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count


def word_count(text):
    word_count =len(text.split())
    return word_count


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


main()


