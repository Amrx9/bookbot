import string

def numbers_words():
    text = get_book_text(book)
    num_words = get_words_num(text)
    print(f"{num_words} Words found on the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_num(text):
    words = text.split()
    return len(words)

def count_chars():
    letters = list(string.ascii_lowercase + string.punctuation + string.whitespace + ' ')
    count_words = {}

    text = get_book_text(book)
    lower_text = text.lower()

    for letter in letters: # a
        counter = 0
        for char in lower_text:
            if letter == char:
                counter += 1
        if counter == 0:
            continue
        else:
            count_words[letter] = counter

    return count_words

def report():

    print(f"--- Begin report of {book} ---")
    numbers_words()
    counts = count_chars()

    for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")

book = "books/frankenstein.txt"

report()