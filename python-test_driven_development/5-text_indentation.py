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

    text = text.strip()
    
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
