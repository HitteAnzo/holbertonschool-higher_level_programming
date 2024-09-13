#!/usr/bin/python3
"""
This module contains the function text_indentation which prints text
with two new lines after specific punctuation marks ('.', '?', ':').
"""

def text_indentation(text):
    """
    Prints a string with two new lines after each '.', '?' and ':'.
    
    Args:
        text (str): The string to be processed.
    
    Raises:
        TypeError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ['.', '?', ':']
    result = ""
    i = 0
    
    while i < len(text):
        result += text[i]
        if text[i] in special_chars:
            result += "\n\n"
            i += 1
            # Skip any spaces after the special character
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
    
    # Print the final result, stripping leading/trailing spaces
    print(result.strip())
