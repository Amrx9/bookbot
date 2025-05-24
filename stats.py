def count_words(text):
    """Count the total number of words in the text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Count frequency of each alphabetic character (case-insensitive)."""
    # Convert to lowercase for case-insensitive counting
    text_lower = text.lower()
    
    # Dictionary to store character counts
    char_counts = {}
    
    # Count each character
    for char in text_lower:
        if char.isalpha():  # Only count alphabetic characters
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    
    return char_counts

def create_character_list(char_counts):
    """Convert character count dictionary to sorted list of dictionaries."""
    char_list = []
    
    # Convert dictionary to list of dictionaries
    for char, count in char_counts.items():
        char_list.append({
            'character': char,
            'count': count
        })
    
    # Sort by count (highest first)
    char_list.sort(key=lambda x: x['count'], reverse=True)
    
    return char_list

def analyze_text(text):
    """
    Analyze text and return word count and character frequency data.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        tuple: (word_count, sorted_character_list)
    """
    # Count words
    word_count = count_words(text)
    
    # Count characters
    char_counts = count_characters(text)
    
    # Create sorted list
    sorted_char_list = create_character_list(char_counts)
    
    return word_count, sorted_char_list