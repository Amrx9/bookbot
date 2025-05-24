def get_words_nums(text):
    words = text.split()
    return len(words)

def get_letter_nums(text):
    lower_letters = text.lower()
    words_nums_dicts = {}
    for letter in lower_letters:
        if letter in words_nums_dicts:
            words_nums_dicts[letter] += 1
        else:
            words_nums_dicts[letter] = 1
    return words_nums_dicts

def sort_on(dict):
    return dict["num"]

def sorted_list_of_dicts(text):
    list_of_dicts = []
    words_count = get_words_nums(text)
    letter_numbers = get_letter_nums(text)
    for key in letter_numbers:
        list_of_dicts.append({"char": key, "num": letter_numbers[key]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts, words_count