import sys
from stats import analyze_text

def read_book(file_path):
    """Read and return the contents of a book file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find file '{file_path}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def print_report(file_path, word_count, character_counts):
    """Print a formatted report of the book analysis."""
    print("=" * 32)
    print("BOOKBOT ANALYSIS")
    print("=" * 32)
    print(f"Analyzing book: {file_path}")
    print()
    print("--- Word Count ---")
    print(f"Total words found: {word_count:,}")
    print()
    print("--- Character Frequency ---")
    
    for char_data in character_counts:
        char = char_data['character']
        count = char_data['count']
        print(f"'{char}' appears {count:,} times")
    
    print("=" * 32)
    print("ANALYSIS COMPLETE")
    print("=" * 32)

def main():
    """Main function to run BookBot analysis."""
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        print("Example: python3 main.py books/frankenstein.txt")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    # Read the book file
    book_text = read_book(file_path)
    if book_text is None:
        sys.exit(1)
    
    # Analyze the text
    word_count, character_counts = analyze_text(book_text)
    
    # Print the results
    print_report(file_path, word_count, character_counts)

if __name__ == "__main__":
    main()
