# book_analyzer.py
import string
from collections import Counter
from typing import Dict

class BookAnalyzer:
    def __init__(self, file_path: str):
        """Initialize BookAnalyzer with a file path."""
        self.file_path = file_path
        self.text = self._read_file()

    def _read_file(self) -> str:
        """Read the contents of the file."""
        try:
            with open(self.file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: Could not find file '{self.file_path}'")
            return ""
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    def count_words(self) -> int:
        """Count total number of words in the text."""
        return len(self.text.split())

    def count_characters(self) -> Dict[str, int]:
        """Count occurrences of each character in the text."""
        # Convert text to lowercase for case-insensitive counting
        text_lower = self.text.lower()
        
        # Create a string of all characters we want to count
        countable_chars = string.ascii_lowercase + string.punctuation + string.whitespace
        
        # Use Counter for efficient character counting
        char_counts = Counter(text_lower)
        
        # Filter out characters we don't want to count and zero counts
        return {char: count for char, count in char_counts.items() 
                if char in countable_chars and count > 0}

    def generate_report(self) -> None:
        """Generate and print the analysis report."""
        if not self.text:
            print("No text to analyze.")
            return

        print(f"\n--- Begin report of {self.file_path} ---")
        
        # Word count
        word_count = self.count_words()
        print(f"Total words found: {word_count}")
        
        # Character count
        char_counts = self.count_characters()
        
        # Sort characters by frequency (highest to lowest)
        sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
        
        print("\nCharacter frequencies:")
        for char, count in sorted_chars:
            if char == ' ':
                char_display = 'space'
            elif char == '\n':
                char_display = 'newline'
            elif char == '\t':
                char_display = 'tab'
            else:
                char_display = char
            print(f"The '{char_display}' character was found {count} times")
            
        print("--- End report ---\n")

# main.py
def main():
    # File path
    book_path = "books/frankenstein.txt"
    
    # Create analyzer and generate report
    analyzer = BookAnalyzer(book_path)
    analyzer.generate_report()

if __name__ == "__main__":
    main()