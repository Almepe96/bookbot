def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = word_count(text)
    each_letter = letter_count(text)            #list of dictionaries
    sorted_letters = sort_letters(each_letter)
    word_report(path, num_words, sorted_letters)


def word_report(path, num_words, each_letter):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    for dict in each_letter:
        for k in dict:
            print(f"The {k} character was found {dict[k]} times")
    print("--- End report ---")

    k, v = dict.items()
    return v



def sort_letters(dict):
    return dict#.sort(key=sort_on, reverse=True)




def letter_count(text):
    letter_count = {}
    letter_list = []
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    for k in letter_count:
        letter_list.append({k:letter_count[k]})
    print (letter_list)
    return letter_list


def word_count(text):
    word_count =len(text.split())
    return word_count


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


main()


