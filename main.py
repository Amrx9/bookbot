from stats import sorted_list_of_dicts

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

letter_numbers, words_nums = sorted_list_of_dicts(get_book_text('books/frankenstein.txt'))
print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(f"Found {words_nums} total words")
print("--------- Character Count -------")
for dict in letter_numbers:
    if dict['char'].isalpha():
        print(f"{dict['char']}: {dict['num']}")
print("============= END ===============")
