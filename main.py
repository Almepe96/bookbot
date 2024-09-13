def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = word_count(text)
    each_letter = letter_count(text)
    sorted_letters = each_letter #meter funcion aqui
    word_report(path, num_words, sorted_letters)


def word_report(path, num_words, each_letter):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")



    for k in each_letter:
        print(f"The {k} character was found {each_letter[k]} times")
    
    
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


